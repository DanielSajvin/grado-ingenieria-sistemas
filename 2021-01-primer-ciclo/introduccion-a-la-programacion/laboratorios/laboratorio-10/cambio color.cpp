#include <iostream>

using namespace std;

int main()
{
	int opcion;
	do
	{
		cout << "Seleccione lo que desee realizar: " << endl;
		cout << "1.  Interfaz predeterminada 1." << endl;
		cout << "2.  Interfaz predeterminada 2." << endl;
		cout << "3.  Interfaz predeterminada 3." << endl;
		cout << "4.  Salir" << endl;
		cin >> opcion;

		if (opcion == 1)
		{
			system("cls");
			cout << "INTERFAZ PREDETERMINADA 1" << endl;
			system("color 2E");

		}

		else if (opcion == 2)
		{
			system("cls");
			cout << "INTERFAZ PREDETERMINADA 2" << endl;
			system("color 4B");
		}

		else if (opcion == 3)
		{
			system("cls");
			cout << "INTERFAZ PREDETERMINADA 3" << endl;
			system("color 1C");
		}

		else if (opcion == 4)
		{
			cout << "SALIENDO...." << endl;
		}

		else
		{
			cout << "OPCION INCORRECTA" << endl;
		}

	} while (opcion != 4);

	system("pause");
	cout << endl << endl;
}