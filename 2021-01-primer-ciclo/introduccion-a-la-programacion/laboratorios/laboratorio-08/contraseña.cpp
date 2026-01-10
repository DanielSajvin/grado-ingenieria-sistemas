#include <iostream>
using namespace std;

int main()
{
	int contra, op, aux, num1, num2, num3;

	bool bandera = false;

	do
	{
		cout << "----------SISTEMA DE CONTRASEÑA----------" << endl << endl;
		cout << "Seleccione una opcion del menu: " << endl;
		cout << "1. Ingresar la clave secreta" << endl;
		cout << "2. Ingresar al sistema" << endl;
		cout << "3. Salir del programa" << endl;
		cin >> op;
		cout << endl << endl;

		//CONDICIONES SEGUN LA OPCION QUE INGRESE EL USUARIO
		if (op == 1)
		{
			//ESTA FUNCION ES POR SI EL USUARIO NO INGRESE LA CLAVE CORRECTA SE LE VA A PEDIR QUE LO HAGA DE NUEVO
			while (bandera == false)
			{
				cout << "Ingrese la contraseña (debe ser un numero de 3 cifras)" << endl;
				cin >> contra;
				if (contra >= 100 && contra <= 999)
				{
					//ESTO ES PARA ROMPER LA FUNCION Y SEGUIR A LO SIGUIENTE 
					bandera = true;
				}
				else
				{
					cout << "CONTRASEÑA INCORRECTA VERIFIQUE QUE CUMPLA CON LOS REQUISITOS VUELVA A INTENTARLO" << endl;
				}
			}
		}

		else if (op == 2)
		{
			//PEDIR LOS NUMEROS POR SEPARADO Y VER SI SON LOS MISMOS DE LA OPCION 1
			
			num1 = contra / 100;
			aux = contra % 100;
			num2 = aux / 10;
			num3 = aux % 10;

			cout << num1 << ", " << num2 << ", " << num3 << endl;
			cout << "CONTRASEÑA CORRECTA.  CREADO POR:  MARIO DANIEL SAJVIN GOMEZ" << endl;

		}

		else if (op == 3)
		{
			cout << "SALIENDO DEL SISTEMA" << endl;
		}
		else
		{
			cout << "OPCION INCORRECTA" << endl;
		}




	} while (op != 3);
}