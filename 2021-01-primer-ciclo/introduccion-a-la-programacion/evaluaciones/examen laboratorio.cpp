#include <iostream>
#include <string>

using namespace std;

int main()
{
	int opcion;
	string nombre[15];
	int edad[15];
	string genero[15];
	int voto[15];
	int contador = 0;
	

	
	do {

		cout << endl << endl << "*****   M E N U   *****" << endl << endl;
		cout << "1.   Inscribir nuevo candidato" << endl;
		cout << "2.   Registrar votacion" << endl;
		cout << "3.   Posiciones" << endl;
		cout << "4.   Listado de candidatos con edad mayor a 40" << endl;
		cout << "5.   Cerrar votaciones" << endl;
		cout << "6.   Salir" << endl;
		cout << "Ingrese la opcion que desea realizar: ";
		cin >> opcion;
		cout << endl;

		if (opcion == 1) 
		{
			cout << "Ingrese nombre del candidato: ";
			cin >> nombre[contador];

			cout << "Ingrese edad: ";
			cin >> edad[contador];

			cout << "Ingrese genero: ";
			cin >> genero[contador];
			contador++;
		}
		else if (opcion == 2)
		{
			int op;
			cout << endl << endl << "Tiene dos opciones que desea hacer..." << endl;
			cout << "1.   Ver los candidatos." << endl;
			cout << "2.   Realizar un voto." << endl;
			cout << "Seleccione la opcion que desee realizar: ";
			cin >> op;
			cout << endl<<endl;
			//MENU PARA QUE VEA PRIMERO LOS CANDIDATOS Y DESPUES PUEDA ELEGIR UNO DE ELLOS
			if (op == 1)
			{

				for (int i = 0; i < contador; i++)
				{
					cout << endl << "Candidato " << i + 1 << endl << endl;
					cout <<  nombre[i] << endl << endl;
				}
			}

			else if (op == 2)
			{
				int contador = 0;
				int voto;
				cout << "Ingrese el numero del canditato por el cual desea votar: ";
				cin >> voto;
				cout << endl << endl;

				for (int i = 0; i < 15; i++)
				{
						if (nombre[i] == voto) 
						{
							contador++;
						}
					
				}

			}
		}

		else if (opcion == 3) 
		{
			int aux;
			for (int i = 0; i < 15; i++)
			{
				for (int j = 0; j < (15 - 1); j++)
				{
				
					// arreglo DESCENDENTE
					if (voto[i] > voto[j])
					{
						aux = voto[i];
						voto[i] = voto[j];
						voto[j] = aux;
					}
				}

			}

			
			cout << endl << endl << "Votaciones ordenadas de Mayor a Menor: " << endl;
			for (int i = 0; i < 5; i++) 
			{
				cout << voto[i] << endl;
			}
			for (int i = 0; i < 5; i++)
			{
				cout << nombre[i] << endl;
			}

			int suma = 0;
			for (int i = 0; i < 2; i++)
			{
				
			      suma = suma + voto[i];
				
			}
			cout << endl << endl<<"La sumatoria es: " << suma << endl;
			cout << "El promedio es: " << (suma / 15) << endl;
			
		}

		else if (opcion == 4)
		{

		}

		else if (opcion == 5)
		{

		}

		
	} while (opcion != 6);

	system("pause");
	cout << endl << endl;
}