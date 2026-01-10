#include <iostream>
#include <time.h>

using namespace std;

int main()
{
	srand(time(NULL));
	int matriz[5][5];

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			matriz[i][j] = -20 + rand() % 41;
		}
	}

	/* ESTA PARTE ES SOLO PARA COMPROBAR QUE SI SE LLENO CORRECTAMENTE LA MATRIZ, LO UTILICE UNICAMENTE PARA IR PROBANDO 
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cout << "posicion " << i << "," << j << " :" << matriz[i][j] << endl;  
		}

	}
	*/

	//EN ESTA PARTE SE IMPRIME LA TABLA COMO TAL 
	for (int i = 0; i < 5; i++)
	{
		cout << matriz[i][0] << "   " << matriz[i][1] << "   " << matriz[i][2] << "   "
			<< matriz[i][3] << "   " << matriz[i][4] << "   " << endl;
	}
	cout << endl;

	//SE UTILIZA UN CONTADOR PARA DETERMINAR LA CANTIDAD DE POSITIVOS Y NEGATIVOS
	int pos = 0, neg = 0;
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (matriz[i][j] > 0)
			{
				pos++;
			}
			else if (matriz[i][j] < 0)
			{
				neg++;
			}
		}
	}

	//IMPRIMIR LO QUE SE REALIZA EN EL CICLO DE ARRIBA
	cout << endl << endl;
	cout << "La cantidad de numero positivos es: " << pos << endl;
	cout << "La cantidad de numeros negativos es: " << neg << endl << endl << endl;

	//SE DECLARA UN CONTADOR PARA IR SUMANDO
	int suma;
	for (int i = 0; i < 5; i++)
	{
		suma = 0;
		for (int j = 0; j < 5; j++)
		{
			suma = suma + matriz[i][j];
		}
		cout << "Sumatoria de la fila No." << i << ": " << suma << endl;
	}
	cout << endl << endl;
	system("pause");



}
