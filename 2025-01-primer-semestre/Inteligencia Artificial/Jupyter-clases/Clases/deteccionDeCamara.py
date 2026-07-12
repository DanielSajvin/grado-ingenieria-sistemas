import cv2
import mediapipe as mp
import math
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def distancia(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)


def palm_normal(lm):
    p0 = np.array([lm[0].x, lm[0].y, lm[0].z])
    p5 = np.array([lm[5].x, lm[5].y, lm[5].z])
    p17 = np.array([lm[17].x, lm[17].y, lm[17].z])

    v1 = p5 - p0
    v2 = p17 - p0
    normal = np.cross(v1, v2)
    return normal / np.linalg.norm(normal)  # vector unitario


def palma_hacia_camara(lm, umbral=-0.2):
    n = palm_normal(lm)
    return n[2] < umbral


def direccion_indice(lm, delta=0.05):
    if lm[8].x < lm[0].x - delta:
        return "izquierda"
    elif lm[8].x > lm[0].x + delta:
        return "derecha"
    else:
        return None


# Funcion para determinar si un dedo esta levantado
def dedos_levantados(landmarks, umbral=0.1):
    # Comparar la posicion "y" del punto a la punta con los puntos anteriores
    dedos = {
        "Pulgar": False,
        "Indice": False,
        "Medio": False,
        "Anular": False,
        "Menique": False,
    }

    # Pulgar (comparacion en eje x para mejor precision)
    dedos["Pulgar"] = (
        landmarks[4].x < landmarks[3].x
        if landmarks[0].x < landmarks[9].x
        else landmarks[4].x < landmarks[3].x
    )

    dedos["Indice"] = landmarks[8].y < landmarks[6].y
    dedos["Medio"] = landmarks[12].y < landmarks[10].y
    dedos["Anular"] = landmarks[16].y < landmarks[14].y
    dedos["Menique"] = landmarks[20].y < landmarks[18].y

    return dedos


def detectar_gesto(dedos, lm):
    indice_ext = dedos["Indice"]
    pulgar_abierto = dedos["Pulgar"]
    otros_cerrados = not any([dedos["Medio"], dedos["Anular"], dedos["Menique"]])
    mano_plana = (
        abs(lm[0].z - lm[9].z) < 0.07
    )  # muñeca y centro de palma casi al mismo Z
    dir_idx = direccion_indice(lm)

    # para detectar corazon coreano
    pulgar_doblado = lm[4].y > lm[3].y
    indice_doblado = lm[8].y > lm[6].y
    puntas_cerca = distancia(lm[4], lm[8]) < 0.04
    otros_cerrados = not any([dedos["Medio"], dedos["Anular"], dedos["Menique"]])

    if all(dedos.values()) and distancia(landmarks[4], landmarks[8]) > 0.18:
        return "Mano Abierta ✋"
    if (
        dedos["Indice"]
        and dedos["Medio"]
        and not any([dedos["Pulgar"], dedos["Anular"], dedos["Menique"]])
    ):
        return "Victoria ✌️"
    if pulgar_doblado and indice_doblado and puntas_cerca and otros_cerrados:
        # opcional: exigir palma hacia la cámara
        if palma_hacia_camara(lm, umbral=-0.1):
            return "Corazón Coreano 💖"

    elif dedos["Pulgar"] and not any(
        [dedos["Indice"], dedos["Medio"], dedos["Anular"], dedos["Menique"]]
    ):
        return "Pulgar Arriba 👍"
    elif (
        any([dedos["Indice"], dedos["Pulgar"]])
        and distancia(landmarks[4], landmarks[8]) < 0.1
    ):
        return "ok 👌"
    elif all(dedos.values()):
        return "Alto ✋"
    elif (
        dedos["Indice"]
        and dedos["Menique"]
        and not any([dedos["Pulgar"], dedos["Medio"], dedos["Anular"]])
    ):
        return "Cuernos 🤘"
    elif (
        dedos["Pulgar"]
        and dedos["Menique"]
        and not any([dedos["Indice"], dedos["Medio"], dedos["Anular"]])
    ):
        return "Llamame 🤙"
    elif (
        dedos["Indice"]
        and dedos["Menique"]
        and dedos["Pulgar"]
        and not any([dedos["Medio"], dedos["Anular"]])
    ):
        return "Te Quiero 🤟"
    elif (
        all(dedos.values())
        and distancia(landmarks[12], landmarks[16])
        > 0.10  # separación entre medio y anular (Vulcano)
        and distancia(landmarks[8], landmarks[12]) < 0.07  # índice-medio juntos
        and distancia(landmarks[16], landmarks[20]) < 0.07  # anular-meñique juntos
        and distancia(landmarks[4], landmarks[8]) > 0.10  # pulgar separado del índice
    ):
        return "Saludo Vulcano 🖖"
    if indice_ext and pulgar_abierto and otros_cerrados and mano_plana and dir_idx:
        if dir_idx == "izquierda":
            return "Señalar Izquierda 👈"
        else:
            return "Señalar Derecha 👉"
        # ─── Mano cerrada / Puño ───
    mano_cerrada = not any(dedos.values())

    if mano_cerrada and palma_hacia_camara(lm, umbral=-0.2):
        return "Puño 👊"
    elif mano_cerrada:
        return "Mano Cerrada ✊"
    elif (
        dedos["Indice"]
        and dedos["Pulgar"]
        and not any([dedos["Medio"], dedos["Anular"], dedos["Menique"]])
        and 0.1 <= distancia(landmarks[4], landmarks[8]) <= 0.18
        and distancia(landmarks[8], landmarks[12]) > 0.06  # índice y medio separados
        and distancia(landmarks[4], landmarks[12]) > 0.10  # pulgar y medio separados
        and not palma_hacia_camara(lm, umbral=-0.3)  # palma no completamente de frente
    ):
        return "Pinza 🤏"
    # Señalar Izquierda: índice y pulgar levantados, índice apuntando a la izquierda
    elif (
        dedos["Indice"]
        and dedos["Pulgar"]
        and not any([dedos["Medio"], dedos["Anular"], dedos["Menique"]])
        and (landmarks[8].x < landmarks[6].x)  # índice apunta a la izquierda
        and (landmarks[4].y > landmarks[3].y)  # pulgar hacia arriba
    ):
        return "Señalar Izquierda 👈"

    else:
        return "Gestos no reconocidos"


# Configurar la captura de la webcam
cap = cv2.VideoCapture(0)  # 0 para la camara predeterminada

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("No se pudo capturar la imagen")
            continue

        # image = cv2.imread(ruta)
        # height, width, _ = image.shape
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hands_landmarks in results.multi_hand_landmarks:
                # Dibujar las marcas y conexiones
                mp_drawing.draw_landmarks(
                    image, hands_landmarks, mp_hands.HAND_CONNECTIONS
                )
                # Obtener las marcas como una lista
                landmarks = hands_landmarks.landmark

                # Indices de los dedos segun mediaPipe
                dedos = dedos_levantados(landmarks)
                gesto = detectar_gesto(dedos, landmarks)

                # Mostrar los dedos levantados en la imagen (opcional)
                info_dedos = f"Dedos: {[k for k, v in dedos.items() if v]}"
                cv2.putText(
                    image,
                    info_dedos,
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (150, 255, 0),
                    2,
                )

                # Mostrar gesto detectado
                cv2.putText(
                    image,
                    f"Gesto: {gesto}",
                    (10, 55),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2,
                )

        # MOSTRAR LA IMAGEN RESULTANTE
        # image = cv2.resize(image, (1000, 800))  # Ajusta a un tamaño más pequeño
        cv2.imshow("Deteccion de Gestos", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
