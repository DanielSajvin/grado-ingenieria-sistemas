#include <iostream>

using namespace std;

int main()
{
	int n1, n2;
	

	cout << "Ingrese un numero entero" << endl;
	cin >> n1;
	cout << endl << endl;

	cout << "Ingrese un numero entero" << endl;
	cin >> n2;
	cout << endl << endl;

	if (n2 > n1)
	{
		while (n1 <= n2)
		{
			if (n1 % 2 == 0)
			{
				cout << n1 << ", ";
			}
			n1++;
		}
	}
	else
	{
		cout << "ERROR, EL PRIMER NUMERO DEBE SER MENOR AL SEGUNDO VUELVA A INTENTARLO" << endl;
	}

	cout << endl;
	system("pause");
	cout << endl << endl;
}