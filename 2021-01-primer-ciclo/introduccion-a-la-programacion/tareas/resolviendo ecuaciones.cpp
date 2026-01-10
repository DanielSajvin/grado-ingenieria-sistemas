#include <iostream>

using namespace std;

int main()
{
	float a, b, c, res, x1, x2;

	cout << "Ingrese el valor de a: " << endl;
	cin >> a;
	cout << endl;

	cout << "Ingrese el valor de b: " << endl;
	cin >> b;
	cout << endl;

	cout << "Ingrese el valor de c: " << endl;
	cin >> c;
	cout << endl;

	//voy a restar el valor de b elevado al cuadrado por 4*a*c
	res = (b * b) - (4 * a * c);
	//aplicando la formula
	x1 = (-b + sqrt(res)) / (2 * a);
	x2 = (-b - sqrt(res)) / (2 * a);

	//resultado
	cout << "Los resultados son :" << endl;
	cout << "x1: " << x1 << endl;
	cout << "x2: " << x2 << endl;

	cout << endl;
	system("pause");
	cout << endl << endl;
}