#include <iostream>

using namespace std;

int main()
{
	int num1, num2;

	cout << "Ingrese el primer numero" << endl;
	cin >> num1;
	cout << endl;

	cout << "Ingrese el numeo limite" << endl;
	cin >> num2;
	cout << endl;

	for (num1; num1 <= num2; num1++)
	{
		if (num1 % 2 != 0)
		{
			cout << num1 << ", " << endl;
		}
	}
	cout << endl;
	system("pause");
	cout << endl;
}