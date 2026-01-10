#include <iostream>

using namespace std;

int main()
{
	int numeros[10];

	for (int i = 0; i < 10; i++)
	{
		do
		{
			cout << "Ingrese 10 numeros enteros: " << endl;
			cin >> numeros[i];

		} while (numeros[i] < 0 || numeros[i] > 10);
	}

	int suma = 0, promedio;

	for (int i = 0; i < 10; i++)
	{
		suma = suma + numeros[i];

	}

	cout << endl << endl << "La sumatoria de los datos ingresados es: " << suma << endl << endl;

	promedio = suma / 10;

	cout << endl << endl << "El promedio de los numeros ingresados es: " << promedio << endl << endl;

	system("pause");
}