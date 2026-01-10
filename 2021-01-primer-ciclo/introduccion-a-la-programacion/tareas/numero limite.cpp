#include <iostream>

using namespace std;

int main()
{
	int num;
	int i = 1;

	cout << "Ingrese un numero limite" << endl;
	cin >> num;
	cout << endl;

	while (i <= num)
	{
		if (i % 2 != 0)
		{
			cout << i << endl;
		}
		i++;
	}
	cout << endl;
	system("pause");
	cout << endl << endl;
}