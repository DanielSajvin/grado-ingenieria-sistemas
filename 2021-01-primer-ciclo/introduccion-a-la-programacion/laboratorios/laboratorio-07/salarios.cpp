#include <iostream>

using namespace std;

int main()
{
	float sal1, sal2, sal3, sal4, sal5;
	int n1, n2, n3;
	int tol = 0;
	int to2 = 0;
	int to3 = 0;

	cout << "Ingrese el salario del primer empleado" << endl;
	cin >> sal1;
	cout << endl;

	cout << "Ingrese el salario del segundo empleado" << endl;
	cin >> sal2;
	cout << endl;

	cout << "Ingrese el salario del tercer empleado" << endl;
	cin >> sal3;
	cout << endl;

	cout << "Ingrese el salario del cuarto empleado" << endl;
	cin >> sal4;
	cout << endl;

	cout << "Ingrese el salario del quinto empleado" << endl;
	cin >> sal5;
	cout << endl;

	//verificar en que puesto esta cada empleado segun su salario

	n1 = 0;
	n2 = 0;
	n3 = 0;

	if (sal1 > 15000)
	{
		n1 = n1 + 1;
	}
	else
	{
		if (sal1 > 7000 && sal1 <= 15000)
		{
			n2 = n2 + 1;
		}
		else {
			if (sal1 > 0 && sal1 <= 7000)
			{
				n3 = n3 + 1;
			}
		}
	}
	if (sal2 > 15000) 
	{
		n1 = n1 + 1;
	}

	else 
	{
		if (sal2 > 7000 && sal2 <= 15000)
		{
			n2 = n2 + 1;
		}
		else 
		{
			if (sal2 > 0 && sal2 <= 7000)
			{
				n3 = n3 + 1;
			}
		}
	}

	if (sal3 > 15000) 
	{
		n1 = n1 + 1;
	}
	else 
	{
		if (sal3 > 7000 && sal3 <= 15000)
		{
			n2 = n2 + 1;
		}
		else
		{
			if (sal3 > 0 && sal3 <= 7000) 
			{
				n3 = n3 + 1;
			}
		}
	}

	if (sal4 > 15000) 
	{
		n1 = n1 + 1;
	}
	else
	{
		if (sal4 > 7000 && sal4 <= 15000)
		{
			n2 = n2 + 1;
		}
		else
		{
			if (sal4 > 0 && sal4 <= 7000) 
			{
				n3 = n3 + 1;
			}
		}
	}

	if (sal5 > 15000) 
	{
		n1 = n1 + 1;
	}
	else 
	{
		if (sal5 > 7000 && sal5 <= 15000)
		{
			n2 = n2 + 1;
		}
		else 
		{
			if (sal5 > 0 && sal5 <= 7000)
			{
				n3 = n3 + 1;
			}
		}
	}
	tol = tol + sal1;
	to2 = to2 + sal2;
	to3 = to3 + sal3;
	cout << "El numero de personas con salario alto es: " << tol << endl;
	cout << "El numero de personas con salario medio es: " << to2 << endl;
	cout << "El numero de personas con salario bajo es:  " << to3 << endl;
	tol = 0;
	to2 = 0;
	to3 = 0;

	cout << endl << endl;
	system("pause");
	cout << endl;

	
	


}