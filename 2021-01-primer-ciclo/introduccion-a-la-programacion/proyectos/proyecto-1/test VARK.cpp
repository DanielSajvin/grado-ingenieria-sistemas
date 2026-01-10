#include <iostream>
using namespace std;

int main()
{
	char p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16;
	int V, A, R, K;
	bool bandera = false;
	

	//VARIABLES PARA GUARDAR LAS RESPUESTAS 
	V = 0;
	A = 0;
	R = 0;
	K = 0;

	cout << "--------------- BIENVENIDO AL TEST VARK ---------------" << endl;
	cout << "Este cuestionario tiene como proposito ayudarle a conocer como trabaja con la" << endl;
	cout << "informacion y cual es su estilo de aprendizaje preferido para captar, procesar, " << endl;
	cout << "proporcionar ideas e informacion." << endl << endl;

	cout << "--------------- INSTRUCCIONES ---------------" << endl;
	cout << "Esta a punto de comenzar el test, se le haran una serie de preguntas." << endl;
	cout << "1.  Seleccione la letra del inciso que usted considere correcta." << endl;
	cout << "2.  Solo puede contestar con una opcion." << endl;
	cout << "3.  Debe escribir la letra del inciso en minuscula." << endl;
	cout << "4.  Para avanzar a la siguiente pregunta presione enter." << endl;
	cout << "Por favor responda lo mas honestamente posible." << endl;
	cout << "¡VAMOS A LAS PREGUNTAS!" << endl;
	cout << endl << endl;

	//INICIO DE LAS PREGUNTAS

	do{
		cout << "1.  Esta ayudando a una persona que desea ir al aeropuerto, al centro de la ciudad o a la" << endl;
		cout << "estacion del ferrocarril, usted... " << endl;
		cout << "a.  Iria con ella" << endl;
		cout << "b.  Le diria como llegar" << endl;
		cout << "c.  Le daria las instrucciones por escrito (sin un mapa)" << endl;
		cout << "d.  Le daria un mapa" << endl;
		cin >> p1;

		//CONDICION PARA IR GUARDANDO Y SUMANDO LAS RESPUESTAS 
		
		bandera;

		if (p1 == 'd')
		{
			V = V + 1;
		}
		else if (p1 == 'b')
		{
			A = A + 1;
		}
		else if (p1 == 'c')
		{
			R = R + 1;
		}
		else if (p1 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p1 != 'a' && p1 != 'b' && p1 != 'c' && p1 != 'd');

	do
	{
		cout << "2.  No esta seguro si una palabra se escribe como *trascendnete* o *tracendnete*, usted..." << endl;
		cout << "a.  Veria las palabras en su mente y eligiria la que mejor luce" << endl;
		cout << "b.  Pensaria en como suena cada palabra y elegiria una " << endl;
		cout << "c.  Las buscaria en un diccionario " << endl;
		cout << "d.  Escribiria ambas palabras y elegiria una " << endl;
		cin >> p2;

		bandera;

		if (p2 == 'a')
		{
			V = V + 1;
		}
		else if (p2 == 'b')
		{
			A = A + 1;
		}
		else if (p2 == 'c')
		{
			R = R + 1;
		}
		else if (p2 == 'd')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p2 != 'a' && p2 != 'b' && p2 != 'c' && p2 != 'd');

	do
	{
		cout << "3.  Esta planeado unas vacaciones para un grupo de personas y desearia la" << endl;
		cout << " retroalimentacion de ellos sobre el plan, usted..." << endl;
		cout << "a.  Describiria algunos de los atractivos del viaje" << endl;
		cout << "b.  Utilizaria un mapa o un sitio web para mostrar los lugares" << endl;
		cout << "c.  Les daria una copia del itinerario impreso" << endl;
		cout << "d.  Les llamaria por telefono, les escribiria o les enviaria un e-mail" << endl;
		cin >> p3;

		bandera;


		if (p3 == 'b')
		{
			V = V + 1;
		}
		else if (p3 == 'd')
		{
			A = A + 1;
		}
		else if (p3 == 'c')
		{
			R = R + 1;
		}
		else if (p3 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p3 != 'a' && p3 != 'b' && p3 != 'c' && p3 != 'd');

	do
	{
		cout << "4.  Va a cocinar algun platillo especial para su familia, usted..." << endl;
		cout << "a.  Cocinaria algo que conoce sin la necesidad de instrucciones" << endl;
		cout << "b.  Pediria sugerencias a sus amigos" << endl;
		cout << "c.  Hojearia un libro de cocina para tomar ideas de las fotografias" << endl;
		cout << "d.  Utilizaria un libro de cocina donde sabe que hay una buena receta" << endl;
		cin >> p4;

		bandera;

		if (p4 == 'c')
		{
			V = V + 1;
		}
		else if (p4 == 'b')
		{
			A = A + 1;
		}
		else if (p4 == 'd')
		{
			R = R + 1;
		}
		else if (p4 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p4 != 'a' && p4 != 'b' && p4 != 'c' && p4 != 'd');

	do
	{
		cout << "5.  Un grupo de turistas desea aprender sobre los parques o las reservas de vida salvaje" << endl;
		cout << "en su area, usted..." << endl;
		cout << "a.  Les daria una platica acerca de parques o reservas de vida salvaje" << endl;
		cout << "b.  Les mostraria figuras de internet, fotografias o libros con imagenes" << endl;
		cout << "c.  Los llevaria a un parque o reserva y daria una caminata con ellos" << endl;
		cout << "d.  Les daria libros o folletos sobre parques o reservas de vida salvaje" << endl;
		cin >> p5; 
			
		bandera;

		if (p5 == 'b')
		{
			V = V + 1;
		}
		else if (p5 == 'a')
		{
			A = A + 1;
		}
		else if (p5 == 'd')
		{
			R = R + 1;
		}
		else if (p5 == 'c')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p5 != 'a' && p5 != 'b' && p5 != 'c' && p5 != 'd');

	do
	{
		cout << "6.  Esta a punto de comprar una camara digital o un telefono movil. ¿Ademas del precio," << endl;
		cout << "que mas influye en su decision" << endl;
		cout << "a.  Lo utiliza o lo prueba" << endl;
		cout << "b.  La lectura de los detalles acerca de las caracteristicas del aparato" << endl;
		cout << "c.  El diseño del aparato es moderno y parece bueno" << endl;
		cout << "d.  Los comentarios del vendedor acerca de las caracteristicas del aparato" << endl;
		cin >> p6;

		bandera;

		if (p6 == 'c')
		{
			V = V + 1;
		}
		else if (p6 == 'd')
		{
			A = A + 1;
		}
		else if (p6 == 'b')
		{
			R = R + 1;
		}
		else if (p6 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p6 != 'a' && p6 != 'b' && p6 != 'c' && p6 != 'd');

	do
	{
		cout << "7.  Recuerde la vez cuando aprendio como hacer algo nuevo. Evite elegir una destreza" << endl;
		cout << "fisica, como bicicleta. ¿Como aprendio mejor?" << endl;
		cout << "a.  Viendo una demostracion" << endl;
		cout << "b.  Escuchando la explicacion de alguien y haciendo preguntas " << endl;
		cout << "c.  Siguiendo pistas visuales en diagramas y graficas" << endl;
		cout << "d.  Siguiendo instrucciones escritas en un manual o libro de texto" << endl;
		cin >> p7;

		bandera;

		if (p7 == 'c')
		{
			V = V + 1;
		}
		else if (p7 == 'b')
		{
			A = A + 1;
		}
		else if (p7 == 'd')
		{
			R = R + 1;
		}
		else if (p7 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p7 != 'a' && p7 != 'b' && p7 != 'c' && p7 != 'd');

	do
	{
		cout << "8.  Tiene un problema con su rodilla. Preferiria que el doctor" << endl;
		cout << "a.  Le diera una direccion web o algo para leer sobre el asunto" << endl;
		cout << "b.  Utilizara un modelo plastico de una rodilla para mostrarle que esta mal" << endl;
		cout << "c.  Le describiera que esta mal" << endl;
		cout << "d.  Le mostrara con un diagrama que es lo que esta mal" << endl;
		cin >> p8;

		bandera;

		if (p8 == 'd')
		{
			V = V + 1;
		}
		else if (p8 == 'c')
		{
			A = A + 1;
		}
		else if (p8 == 'a')
		{
			R = R + 1;
		}
		else if (p8 == 'b')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p8 != 'a' && p8 != 'b' && p8 != 'c' && p8 != 'd');

	do
	{
		cout << "9.  Desea aprender un nuevo programa, habilidad o juego de computadora, usted..." << endl;
		cout << "a.  Leer las instrucciones escritas que vienen con el programa" << endl;
		cout << "b.  Platicar con personas que conocen el programa" << endl;
		cout << "c.  Utilizar los controles o el teclado" << endl;
		cout << "d.  Seguir los diagramas del libro que vienen con el programa" << endl;
		cin >> p9;

		bandera;

		if (p9 == 'd')
		{
			V = V + 1;
		}
		else if (p9 == 'b')
		{
			A = A + 1;
		}
		else if (p9 == 'a')
		{
			R = R + 1;
		}
		else if (p9 == 'c')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p9 != 'a' && p9 != 'b' && p9 != 'c' && p9 != 'd');

	do
	{
		cout << "10.  Le gustan los sitios web que tienen..." << endl;
		cout << "a.  Cosas que se pueden picar, mover o probar" << endl;
		cout << "b.  Un diseño interesante y caracteristicas visuales" << endl;
		cout << "c.  Descripciones escritas interesantes, caracteristicas y explicaciones" << endl;
		cout << "d.  Canales de audio para oir musica, programas o entrevistas" << endl;
		cin >> p10;

		bandera;

		if (p10 == 'b')
		{
			V = V + 1;
		}
		else if (p10 == 'd')
		{
			A = A + 1;
		}
		else if (p10 == 'c')
		{
			R = R + 1;
		}
		else if (p10 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p10 != 'a' && p10 != 'b' && p10 != 'c' && p10 != 'd');

	do
	{
		cout << "11.  Ademas del precio. ¿Que influira mas en su decision de comprar un nuevo libro de no" << endl;
		cout << "ficcion..." << endl;
		cout << "a.  La apariencia le resulta atractiva" << endl;
		cout << "b.  Una lectura rapida de algunas partes del libro" << endl;
		cout << "c.  Un amigo le habla del libro y se lo recomienda" << endl;
		cout << "d.  Tiene historias, experiencias y ejemplos de la vida real" << endl;
		cin >> p11;

		bandera;

		if (p11 == 'a')
		{
			V = V + 1;
		}
		else if (p11 == 'c')
		{
			A = A + 1;
		}
		else if (p11 == 'b')
		{
			R = R + 1;
		}
		else if (p11 == 'd')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p11 != 'a' && p11 != 'b' && p11 != 'c' && p11 != 'd');

	do
	{
		cout << "12.  Esta utilizando un libro, CD o sitio web para aprender como tomar fotografias con su" << endl;
		cout << "nueva camara digital. Le gustaria tener..." << endl;
		cout << "a.  La oportunidad de hacer preguntas y que le hablen sobre las camaras y sus caracteristicas" << endl;
		cout << "b.  Instrucciones escritas con claridad, con caracteristicas y puntos sobre que hacer" << endl;
		cout << "c.  Diagramas que muestren la camara y que hace cada una de sus partes" << endl;
		cout << "d.  Muchos ejemplos de fotografias buenas y malas y como mejorar estas" << endl;
		cin >> p12;

		bandera;

		if (p12 == 'c')
		{
			V = V + 1;
		}
		else if (p12 == 'a')
		{
			A = A + 1;
		}
		else if (p12 == 'b')
		{
			R = R + 1;
		}
		else if (p12 == 'd')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p12 != 'a' && p12 != 'b' && p12 != 'c' && p12 != 'd');

	do
	{
		cout << "13.  Prefiere a un profesor o un expositor que utiliza..." << endl;
		cout << "a.  Demostraciones, modelos o sesiones practicas" << endl;
		cout << "b.  Preguntas y respuestas, charlas, grupos de discusion u oradores invitados" << endl;
		cout << "c.  Folletos, libros o lecturas" << endl;
		cout << "d.  Diagramas, esquemas o graficas" << endl;
		cin >> p13;

		bandera;

		if (p13 == 'd')
		{
			V = V + 1;
		}
		else if (p13 == 'b')
		{
			A = A + 1;
		}
		else if (p13 == 'c')
		{
			R = R + 1;
		}
		else if (p13 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p13 != 'a' && p13 != 'b' && p13 != 'c' && p13 != 'd');

	do
	{
		cout << "14.  Ha acabado una competencia o una prueba y quisiera una retroalimentacion. Quisiera " << endl;
		cout << "tener la retoalimentacion..." << endl;
		cout << "a.  Utilizando ejemplos de lo que ha hecho" << endl;
		cout << "b.  Utilizando una descripcion escrita de sus resultados" << endl;
		cout << "c.  Escuchando a alguien haciendo una revision detallada de su desempeño" << endl;
		cout << "d.  Utilizando graficas que muestren lo que ha conseguido" << endl;
		cin >> p14;

		bandera;

		if (p14 == 'd')
		{
			V = V + 1;
		}
		else if (p14 == 'c')
		{
			A = A + 1;
		}
		else if (p14 == 'b')
		{
			R = R + 1;
		}
		else if (p14 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p14 != 'a' && p14 != 'b' && p14 != 'c' && p14 != 'd');

	do
	{
		cout << "15.  Va a elegir sus alimentos en un restaurante o cafe, usted..." << endl;
		cout << "a.  Elegiria algo que ya ha probado en ese lugar" << endl;
		cout << "b.  Escucharia al mesero o pediria recomendaciones a sus amigos" << endl;
		cout << "c.  Elegiria a partir de las descripciones del menu" << endl;
		cout << "d.  Observaria lo que otros estan comiendo o las fotografias de cada platillo" << endl;
		cin >> p15;

		bandera;

		if (p15 == 'd')
		{
			V = V + 1;
		}
		else if (p15 == 'b')
		{
			A = A + 1;
		}
		else if (p15 == 'c')
		{
			R = R + 1;
		}
		else if (p15 == 'a')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p15 != 'a' && p15 != 'b' && p15 != 'c' && p15 != 'd');

	do
	{
		cout << "16.  Tiene que hacer un discurso importante para una conferencia o una ocasion especial," << endl;
		cout << "usted..." << endl;
		cout << "a.  Elaboraria diagramas o conseguiria graficos que le ayuden a explicar las ideas" << endl;
		cout << "b.  Escribiria algunas palabras clave y practica su discurso repetidamente" << endl;
		cout << "c.  Escribiria su discurso y se lo aprenderia leyendolo varias veces" << endl;
		cout << "d.  Conseguiria muchos ejemplos e historias para hacer la charla real y practica" << endl;
		cin >> p16;

		bandera;

		if (p16 == 'a')
		{
			V = V + 1;
		}
		else if (p16 == 'b')
		{
			A = A + 1;
		}
		else if (p16 == 'c')
		{
			R = R + 1;
		}
		else if (p16 == 'd')
		{
			K = K + 1;
		}
		else
		{
			cout << "ERROR VERIFIQUE SU RESPUESTA" << endl << endl;
		}
		system("cls");
	} while (p16 != 'a' && p16 != 'b' && p16 != 'c' && p16 != 'd');



	//VAMOS A PONER CONDICIONES PARA DETERMINAR CUAL ES EL METODO DE APRENDIZAJE DEL USUARIO
	if (V > A && V > R && V > K)
	{
		cout << endl << endl << "El metodo de parendizaje que usted utiliza es, VISUAL" << endl<< endl;
		cout << "--------------- CARACTERISTICAS ---------------" << endl;
		cout << "Eres una persona muy observadora." << endl;
		cout << "Presentas una facilidad especial para recordar imagenes (y videos)." << endl;
		cout << "Tienes mucha imaginacion y generas imagenes vividas en tu mente." << endl;
		cout << "Las imagenes y los esquemas te van bien para estudiar y memorizar." << endl;
		cout << "Presentas dificultades para recordar o explicar información verbal." << endl << endl;
		cout << "--------------- RECOMENDACIONES ---------------" << endl;
		cout << "Utilice resaltadores." << endl;
		cout << "Cree mapas conceptuales e infografias." << endl;
		cout << "Minimice las distracciones." << endl;
		cout << "Trate de toma notas a mano" << endl;
		cout << "" << endl;
	}
	else if (A > V && A > R && A > K)
	{
		cout << endl << endl << "El metodo de aprendizaje que usted utiliza es, AUDITIVO" << endl << endl;
		cout << "--------------- CARACTERISTICAS ---------------" << endl;
		cout << "Aprendes facilmente al prestar atención a lo que se dice o se narra." << endl;
		cout << "Se te da bien los examenes orales y las presentaciones. " << endl;
		cout << "Eres bueno en relatar narraciones, historias y cuentos. " << endl;
		cout << "Te gusta estudiar con musica y puedes recordar datos y personas con ella." << endl;
		cout << "Eres capaz de recordar signos audibles con cambios de tono de voz, entonaciones y acentos. " << endl <<endl;
		cout << "--------------- RECOMENDACIONES ---------------" << endl;
		cout << "Reproducir música clásica de fondo cuando se estudia." << endl;
		cout << "Trate de realizar debates o equipos de oratoria." << endl;
		cout << "Leer a los demás." << endl;
		cout << "Estudio en grupos o con otra persona para que la gente le haga preguntas en voz alta." << endl;
	}
	else if (R > A && R > V && R > K)
	{
		cout << endl << endl << "----- El metodo de aprendizaje que usted utiliza es, LEER Y ESCRIBIR -----" << endl << endl;
		cout << "--------------- CARACTERISTICAS ---------------" << endl;
		cout << "Le gusta leer." << endl;
		cout << "Le gusta tomar nota de todo." << endl;
		cout << "Para aprender algo prefiere un manual o libro para leer y seguir instrucciones" << endl;
		cout << "Suele consultar sus apuntes y resuelve sus dudas." << endl;
		cout << "Se le da bien la escritura y todo se le facilita con ello." << endl << endl;
		cout << "--------------- RECOMENDACIONES ---------------" << endl;
		cout << "Para estudiar y aprednder mejor, tome nota lo que considere mas importante" << endl;
		cout << "Lea libros, revistas o sitios web para ampliar sus conocimiento" << endl;
		cout << "Los apuntes que realice hagalos en orden para que sea facil su comprension" << endl;
		cout << "Haga resumenes con lo mas importante de los temas" << endl;
	}

	else if (K > A && K > R && K > V)
	{
		cout << endl << endl << "El metodo de aprendizaje que usted utiliza es, KINESTESICO" << endl << endl;
		cout << "--------------- CARACTERISTICAS ---------------" << endl;
		cout << "Tus movimientos son una extension de tus pensamientos creativos." << endl;
		cout << "Tienes la necesidad de expresarte de forma corporal." << endl;
		cout << "Eres una persona inquieta, que se mueve constantemente al hacer tarea o concentrarse" << endl;
		cout << "en una actividad. " << endl;
		cout << "Necesitas involucrarte en lo que estás aprendiendo, de lo contrario, te cuesta mucho" << endl;
		cout << "y se convierte en algo cansado." << endl;
		cout << "Te gusta aprender a través de experiencias, como prácticas en laboratorio, juegos," << endl;
		cout << "modelos, incluso representaciones tangentes de lo que estudias." << endl;
		cout << "--------------- RECOMENDACIONES ---------------" << endl;
		cout << "Haga mapas mentales." << endl;
		cout << "Incluya ejercicios o actividades fisicas que lo ayuden a concentrarse." << endl;
		cout << "Ponga en practica todo lo aprendido, equivocarse es parte del proceso." << endl;
		cout << "Trate de ser mas dinamico, no solo lea ni escriba, porque se terminara aburriendo." << endl;
	}
    cout << endl;
	cout << "---------- FIN DEL TEST, QUE PASE UN BONITO DIA :) ----------" << endl << endl;

	system("pause");
	cout << endl << endl << endl;
}