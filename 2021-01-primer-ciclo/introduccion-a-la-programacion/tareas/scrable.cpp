#include <iostream>
#include <string>

using namespace std;

int main()
{
	int puntaje=0, p2=0,p3=0,p4=0,p5=0, p6=0, p7=0;

	string cadena;

	cout << "*****   S C R A B L E   *****" << endl << endl;
	cout << "A continuacion debe ingresar una palabra, cada letra tiene un valor" << endl;
	cout << "dependiendo de la palabra que ingrese se ira sumando el valor de cada letra." << endl;
	cout << "Ingrese una palabra: " << endl;
	cin >> cadena;
	cout << endl << endl;

	for (int i = 0; i < cadena.length(); i++)
	{
		if (cadena[i] == 'a' || cadena[i] == 'e' || cadena[i] == 'o' || cadena[i] == 's' || cadena[i] == 'i' || cadena[i] == 'u' || cadena[i] == 'n' || cadena[i] == 'l' || cadena[i] == 'r' || cadena[i] == 't' || cadena[i] == 'A' || cadena[i] == 'E' || cadena[i] == 'O' || cadena[i] == 'S' || cadena[i] == 'I' || cadena[i] == 'U' || cadena[i] == 'N' || cadena[i] == 'L' || cadena[i] == 'R' || cadena[i] == 'T')
		{
			puntaje++;
		}

		else if (cadena[i] == 'c' || cadena[i] == 'd' || cadena[i] == 'g' || cadena[i] == 'C' || cadena[i] == 'D' || cadena[i] == 'G' )
		{
			p2 = p2 + 2;
		}

		else if (cadena[i] == 'm' || cadena[i] == 'b' || cadena[i] == 'p' || cadena[i] == 'M' || cadena[i] == 'B' || cadena[i] == 'P')
		{
			p3 = p3 + 3;
		}

		else if (cadena[i] == 'f' || cadena[i] == 'h' || cadena[i] == 'v' || cadena[i] == 'y' || cadena[i] == 'F' || cadena[i] == 'H' || cadena[i] == 'V' || cadena[i] == 'Y')
		{
			p4 = p4 + 4;
		}

		else if (cadena[i] == 'j' || cadena[i] == 'J')
		{
			p5 = p5 + 5;
		}

		else if (cadena[i] == 'k' || cadena[i] == 'll' || cadena[i] == 'ñ' || cadena[i] == 'q' || cadena[i] == 'rr' || cadena[i] == 'w' || cadena[i] == 'x' || cadena[i] == 'K' || cadena[i] == 'LL' || cadena[i] == 'Ñ' || cadena[i] == 'Q' || cadena[i] == 'RR' || cadena[i] == 'W' || cadena[i] == 'X')
		{
			p6 = p6 + 8;
		}

		else if (cadena[i] == 'z' || cadena[i] == 'Z')
		{
			p7 = p7 + 10;
		}
	}

	cout << "El punteo de la palabra ingresada es: " << puntaje+p2+p3+p4+p5+p6+p7 << endl <<endl;


	system("pause");
}