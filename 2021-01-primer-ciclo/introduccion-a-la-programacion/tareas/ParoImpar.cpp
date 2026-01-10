#include <iostream>

using namespace std;

int main()
{
	int num1;
	
	cout << "Ingrese un numero" << endl;
	cin >> num1;

	if (num1 % 2 == 0)
	{
		cout << "Es un numero par" << endl;
	}
	else
	{
		cout << "Es un numero impar" << endl;
	}

	cout << endl;
	system("pause");
	cout << endl << endl;

}