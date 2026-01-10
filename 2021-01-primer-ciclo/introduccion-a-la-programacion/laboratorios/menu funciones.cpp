#include <iostream>

using namespace std;

int triangulorectangulo(int catea, int cateb)
{
	int res;
	res = sqrt((catea * catea) + (cateb * cateb));
	return res;
}

float mayor(float num1, float num2, float num3)
{
	int res;

	if (num1 > num2 && num1 > num3)
	{
		res = num1;
	}
	else if (num2 > num1 && num2 > num3) 
	{
		res = num2;
	}
	else if (num3 > num1 && num3 > num2)
	{
		res = num3;
	}
	else 
	{
		res = 0;
	}
	return res;
}

int main()
{
	int op, catea, cateb, num1, num2, num3;
	float resultado;
	bool bandera = false;

	do
	{
		cout << "---------- MENU ----------" << endl << endl;
		cout << "Seleccione la opcion que desea realizar: " << endl;
		cout << "1.  Hipotenusa" << endl;
		cout << "2.  Mayor" << endl;
		cout << "3.  Salir" << endl;
		cin >> op;
		cout << endl << endl;

		if (op == 1)
		{
			
			
				cout << "Ingrese el cateto a" << endl;
				cin >> catea;
				cout << endl;
				cout << "Ingrese el cateto b" << endl;
				cin >> cateb;
				cout << endl << endl;
				cout << "La hipotenusa es: " << triangulorectangulo(catea, cateb);
			
		}
		////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		else if (op == 2)
		{
			cout << "Ingrese el primer numero: " << endl;
			cin >> num1;
			cout << endl;
			cout << "Ingrese el segundo numero: " << endl;
			cin >> num2;
			cout << endl;
			cout << "Ingrese el tercer numero: " << endl;
			cin >> num3;
			cout << endl << endl;
			resultado = mayor(num1, num2, num3);
			
			cout << "El numero mayor es: " << resultado;
		}

		else if (op == 3)
		{
			cout << "SALIENDO.........." << endl;
		}
	} while (op != 3);

}