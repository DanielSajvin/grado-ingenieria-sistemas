#include <iostream>

using namespace std;

int main()
{
	char letra;

	cout << "Ingrese una letra" << endl;
	cin >> letra;
	cout << endl;

	//como saber si es una vocal o no 

	if (letra == 'A' || letra =='a' || letra == 'E' || letra == 'e' || letra == 'I' || letra == 'i' || letra == 'O' || letra == 'o' || letra == 'U' || letra == 'u')
	{
		cout << "Es una vocal" << endl;
	}
	else
	{
		cout << "Es una consonante" << endl;
	}
	cout << endl << endl;

	system("pause");
	cout << endl << endl;
		
}