#include <iostream>

using namespace std;

int main()
{
	int num, p1, p2, p3;
	float aux;

	cout << "Ingrese un numero de 3 cifras: " << endl;
	cin >> num;

	p1 = num / 100;
	p2 = (num - (p1 * 100)) / 10;
	p3 = (num - (p1 * 100 + p2 * 10));


	cout <<"Las centenas son: " << p1 << endl;
	cout <<"Las decenas son: " << p2 << endl;
	cout << "Las unidades son: " << p3 << endl;

	cout << endl;
	system("pause");
	cout << endl << endl;




}