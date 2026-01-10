#include <iostream>

using namespace std;

int main()
{
	int d1, d2, m1, m2;

	cout << "PRIMERA FECHA" << endl;
	cout << "Ingrese el dia: " << endl;
	cin >> d1;
	cout << endl;
	cout << "Ingrese el mes: " << endl;
	cin >> m1;
	cout << endl;

	cout << "SEGUNDA FECHA" << endl;
	cout << "Ingrese el dia: " << endl;
	cin >> d2;
	cout << endl;
	cout << "Ingrese el mes: " << endl;
	cin >> m2;
	cout << endl;

	if ((m1 - 5) < (m2 - 5))
	{
		cout << "FECHA 1 es mas cercana";
	}
	else if ((m1 - 5) > (m2 - 5))
	{
		cout << "FECHA 2 es mas cercana";
	}
	else 
	{
		//meses son iguales
		if ((d1 - 4) < (d2 - 4))
		{
			cout << "FECHA 1 es mas cercana";
		}
		else if ((d1 - 4) > (d2 - 4)) 
		{
			cout << "FECHA 2 es mas cercana";
		}
		else 
		{
			//FECHAS IGUALES
			cout << "AMBAS FECHAS SON IDENTICAS";
		}

	}
	cout << endl << endl;
	system("pause");
}
	

	


