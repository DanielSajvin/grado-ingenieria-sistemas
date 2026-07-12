import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


# Función para calcular distancia entre puntos
def distancia(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)


# Función para detectar si un dedo está levatnado
def dedo_levantado(landmarks):
    dedos = {
        "Pulgar": False,
        "Indice": False,
        "Medio": False,
        "Anular": False,
        "Menique": False,
    }
    # pulgar (comparacion en eje X para mejor precision)
    dedos["Pulgar"] = (
        landmarks[4].x < landmarks[3].x
        if landmarks[0].x < landmarks[9].x
        else landmarks[4].x > landmarks[3].x
    )
    dedos["Indice"] = landmarks[8].y < landmarks[6].y
    dedos["Medio"] = landmarks[12].y < landmarks[10].y
    dedos["Anular"] = landmarks[16].y < landmarks[14].y
    dedos["Menique"] = landmarks[20].y < landmarks[18].y
    return dedos


# Función para detectar gestos
def detectar_gesto(dedos):
    # Gestos predefinidos
    if (
        dedos["Indice"]
        and dedos["Medio"]
        and not any([dedos["Pulgar"], dedos["Anular"], dedos["Menique"]])
    ):
        return "Victoria ✌️"
    elif dedos["Pulgar"] and not any(
        [dedos["Indice"], dedos["Medio"], dedos["Anular"], dedos["Menique"]]
    ):
        return "Pulgar Arriba 👍"
    elif (
        all([dedos["Medio"], dedos["Anular"], dedos["Menique"]])
        and distancia([landmarks[4], landmarks[8]]) < 0.05
    ):
        return "OK 👌"
    elif all(dedos.values()):
        return "Mano Abierta 👋"
    elif not any(dedos.values()):
        return "Puño Cerrado ✊"
    else:
        return "Gestos no reconocidos"


# configurar la captura de la webcam
cap = cv2.VideoCapture(0)  # 0 para la webcam por defecto

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("No se puede acceder a la cámara.")
            continue

        # voltear la imagen para una mejor visualización
        image = cv2.flip(image, 1)

        # convertir la imagen a RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # procesar la imagen con mediapipe
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # dibujar los puntos de referencia de la mano
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

                # obtener los puntos de referencia de la mano
                landmarks = hand_landmarks.landmark

                # idices de los dedos segun Mediapipe
                dedos = dedo_levantado(landmarks)
                gesto = detectar_gesto(dedos)

                # mostrar gesto detectado
                cv2.putText(
                    image,
                    f"Gesto: {gesto}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

        # mostrar la imagen
        cv2.imshow("Hand Gesture Recognition", image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
