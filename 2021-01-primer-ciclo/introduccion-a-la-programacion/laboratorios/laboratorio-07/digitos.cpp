#include <iostream>

using namespace std;

int main()
{
	int num,n1,n2, n3, aux, op;

	cout << "Ingrese un número de 3 cifras: " << endl;
	cin >> num;
	cout << endl;

	

	
		//procedimiento para separar los numeros
	
		n1 = num / 100;
		aux = num % 100;
		n2 = aux / 10;
		n3 = aux % 10;

		op = pow(n1, 3) + pow(n2, 3) + pow(n3, 3);

		if (num == op)
		{
			cout << "SI es numero de amstrong" << endl;
		}
		else {
			cout << "NO es numero de amstrong" << endl;
		}

	
	cout << endl << endl;
	system("pause");
}