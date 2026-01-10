#include <iostream>

using namespace std;

int main()
{
	float v1, años, salario, salario2, salario3, salario4;

	cout << "Ingrese su sueldo actual" << endl;
	cin >> v1;

	cout << "Ingrese el total de años que lleva laborando" << endl;
	cin >> años;

	if (años > 10)
	{
		salario = v1 + 0.10 * v1;
		cout << "Su salario sera de: Q. " << salario << endl;
	}
	else if (años <= 10 && años > 5)
	{
		salario2 = v1 + 0.07 * v1;
		cout << "Su salario sera de: Q. " << salario2 << endl;
	}
	else if (años <= 5 && años >= 3)
	{
		salario3 = v1 + 0.05 * v1;
		cout << "Su salario sera de: Q. " << salario3 << endl;
	}
	if (años < 3)
	{
		salario4 = v1 + 0.03 * v1;
		cout << "Sulario sera de: Q. " << salario4 << endl;
	}
	cout << endl << endl;
	cout << "PROGRAMA FINALIZADO" << endl;
	
	system("pause");

}