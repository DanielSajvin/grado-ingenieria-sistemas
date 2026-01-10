#include <iostream>

using namespace std;

int main()
{
	int num, num1,num2, num3, num4, aux;

	cout << "Ingrese un numero de 4 cifras: " << endl;
	cin >> num;
	cout << endl;

	//validacion de que se ingrese un numero de 4 cifras
	if (num >= 1000 && num <= 9999)
	{
		num1 = num / 1000;
		aux = num % 1000;
        num2 = aux / 100;
		aux = aux % 100;
        num3 = aux / 10;
		num4 = aux % 10;

		cout << "El orde inverso es: " << endl;
		cout << num4 << num3 << num2 << num1;
		
	}
	else
	{
		cout << "NUMERO INVALIDO, VERIFIQUE QUE SEA DE 4 CIFRAS" << endl;
	}

	cout << endl;
	system("pause");
	cout << endl << endl;
}