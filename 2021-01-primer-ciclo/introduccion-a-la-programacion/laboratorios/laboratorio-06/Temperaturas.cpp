#include <iostream>

using namespace std;

int main()
{
	float v1, temp;

	cout << "Ingrese una temperatura" << endl;
	cin >> v1;

	if (v1 > 100)
	{
		cout << "Arriba del punto de ebullicion del agua" << endl;
	}
	else
	{
		cout << "Abajo del punto de ebullicion del agua" << endl;
	}
	
	cout << endl << endl;
	system("pause");
	
}