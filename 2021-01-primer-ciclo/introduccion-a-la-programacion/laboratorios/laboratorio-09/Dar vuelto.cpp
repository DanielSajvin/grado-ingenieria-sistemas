#include <iostream>

using namespace std;

int main()
{
	float pago, monto, vuelto;
	int num1, num2, num3, num4=0, num5=0, num6=0, aux, res;

	cout << "Ingrese el total a pagar: " << endl;
	cin >> pago;
	cout << endl << endl;

	cout << "Ingrese el monto total (el billete con el que pago el cliente): " << endl;
	cin >> monto;
	cout << endl << endl;

	//RESTA PARA SABER CUANTO SE TIENE QUE DAR DE VUELTO
	res = monto - pago;

	//ACA TENEMOS LA CANTIDAD DIVIDIDA EN CENTENEAS, DECENAS Y UNIDADES
	num1 = res / 100;
	aux = res % 100;
	num2 = aux / 10;
	num3 = aux % 10;

	//COMO YA TENEMOS LOS BILLETES DE 100, 10 Y DE 1, AHORA HAY QUE SACAR LOS DE 50, 20 Y 5


	if (num2 >= 5)
	{
		num4 = num2 / 5;
		num5 = num2 % 5;
	}
	else if (num3 > 5)
	{
		num6 = num3 / 5;
		num3 = num3 % 5;
	}
	cout << "--- En algunos casos tendra dos opciones para dar vuelto usted elige una de las dos opciones ---" << endl << endl;
	cout << "El total de vuelto es: " << res << endl << endl;
	cout << "Billetes de Q100: " << num1 << endl;
	cout << "Billetes de Q50: " << num4 << endl;
	cout << "Billetes de Q20: " << num5 << endl;
	cout << "Billetes de Q10: " << num2 << endl;
	cout << "Billetes de Q5: " << num6 << endl;
	cout << "Billetes de Q1: " << num3 << endl;



	cout << endl;
	system("pause");
	cout << endl << endl;
		
	
		
}