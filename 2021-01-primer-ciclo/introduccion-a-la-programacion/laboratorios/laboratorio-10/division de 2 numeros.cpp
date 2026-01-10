#include <iostream>

using namespace std;

int main()
{
	int a, b, num1 = 1, num2 = 0;

	cout << "Ingrese un numero" << endl;
	cin >> a;
	cout << endl;

	cout << "Ingrese segundo numero" << endl;
	cin >> b;
	cout << endl;

	if (a > b)
	{
		if (a >= b)
		{
			while ((a - b) >= num2)
			{
				num2 = b * num1;
				num1++;
			}
			num1 = num1 - 1;
			num2 = a - num2;


			cout << "El cociente es: " << num1 << endl;
			cout << "Y el residuo es: " << num2 << endl;
		}
	}
	else
	{
		cout << "ERROR EL DIVIDENDO DEBE SER MAYOR AL DIVISOR" << endl;
	}

	cout << endl << endl;
	system("pause");
	cout << endl << endl;
}