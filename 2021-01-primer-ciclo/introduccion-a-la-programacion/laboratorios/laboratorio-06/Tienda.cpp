#include <iostream>

using namespace std;

int main()
{
	int v1, pre;

	cout << "Ingrese la cantidad de teclados que desea adquirir" << endl;
	cin >> v1;

	if (v1 > 7)
	{
		pre = v1 * 100;
		cout << "Su total a pagar es: Q." << pre << endl;
	}
	if (v1 > 3 &&  v1 < 8)
	{
		pre = v1 * 110;
		cout << "Su total a pagar es: Q. " << pre << endl;
	}
	if (v1 < 3)
	{
		pre = v1 * 150;
		cout << "Su total a pagar es: Q. " << pre << endl;
	}
	


	cout << endl << endl;
	system("pause");
	cout << endl;


}