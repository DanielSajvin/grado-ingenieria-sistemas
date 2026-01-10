#include <iostream>

using namespace std;

int main()
{
	int  v1, seg, min, hora, aux;

	cout << "Ingrese una cantidad de segundo: " << endl;
	cin >> v1;
	cout << endl;
	// conversion de segundos a hora, minuto, segundos 
	seg = v1 % 60;
	aux = v1 / 60;

	min = aux % 60;
	
    hora = aux / 60;

	

	if (hora <= 10)
	{
		cout << "Horario de desayuno" << endl;
	}
	if (hora >= 11 && hora  <= 17)
	{
		cout << "Horario de almuerzo" << endl;
	}
	if (hora >= 18 && hora <= 23)
	{
		cout << "Horario de cena" << endl;
	}
	
	


	
	cout << endl;
	system("pause");
	cout << endl << endl;

}