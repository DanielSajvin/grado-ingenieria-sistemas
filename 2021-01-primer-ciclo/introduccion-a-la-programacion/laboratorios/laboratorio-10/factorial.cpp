#include <iostream>

using namespace std;

int main()
{
	int n, i, factorial=1;

	cout << "Ingrese el numero del cual desea saber el factorial" << endl;
	cin >> n;
	cout << endl;

	for (i = 1; i <= n; i++)
	{
		factorial = factorial * i;
	}
	
	cout << "El factorial es de: " << factorial << endl;
	cout << endl << endl;
	system("pause");
}