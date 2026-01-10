#include <iostream>

using namespace std;

int main()
{
	float x, y, x1, y1;

	//primera entrada de datos
	cout << "Ingrese la coordenada x: " << endl;
	cin >> x;
	cout << endl;

	cout << "Ingrese la coordenada y: " << endl;
	cin >> y;
	cout << endl;

	//segunda entrada de datos
	cout << "Ingrese la coordenada x: " << endl;
	cin >> x1;
	cout << endl;

	cout << "Ingrese la coordenada y: " << endl;
	cin >> y1;
	cout << endl;

	//coordenadas de los puntos
	cout << "La coordenada 1 es:" << endl;
	cout << "( " << x << " , " << y << " )" << endl;

	cout << "La coordenada 2 es:" << endl;
	cout << "( " << x1 << " , " << y1 << " )" << endl;

	//vector resultante
	cout << "El vector resultante es:" << endl;
	cout << "(" << (x1 - x) << "," << (y1 - y) << ")" << endl << endl;

	//distancia entre puntos
	cout << "Vector resultante" << endl;
	cout << "(" << (x1 - x) << "," << (y1 - y) << ")" << endl << endl;

	//verificacion si cada una de las coordenadas pertencen a los cuadrantes 
	cout << "Coordenada 1:  ";
	if (x1 > 0 && y1 > 0) {
		cout << "cuadrante 1";
	}
	else if (x1 < 0 && y1 > 0) {
		cout << "cuadrante 2";
	}
	else if (x1 < 0 && y1 < 0) {
		cout << "cuadrante 3";
	}
	else if (x1 > 0 && y1 < 0) {
		cout << "cuadrante 4";
	}

	cout << endl << "Coordenada 2:  ";
	if (x1 > 0 && y1 > 0) {
		cout << "cuadrante 1";
	}
	else if (x1 < 0 && y1> 0) {
		cout << "cuadrante 2";
	}
	else if (x1 < 0 && y1 < 0) {
		cout << "cuadrante 3";
	}
	else if (x1 > 0 && y1 < 0) {
		cout << "cuadrante 4";
	}


	cout << endl << endl;
	system("pause");

}