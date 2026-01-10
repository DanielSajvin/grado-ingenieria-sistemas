#include <iostream>

using namespace std;

int main()
{
	float ra, altu, vol;

	cout << "Ingrese la altura del cilindro en centimetros" << endl;
	cin >> altu;
	cout << endl;

	cout << "Ingrese el radio del cilindro en centimetros" << endl;
	cin >> ra;
	cout << endl;

	//formula para calcular en volumen del cilindro
	vol = 3.1416 * pow (ra,2) * altu;

	cout << "El volumen del cilindro es: " << vol << " cm^3" << endl << endl;

	system("pause");
	cout << endl << endl;



}