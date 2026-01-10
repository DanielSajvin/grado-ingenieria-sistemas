#include <iostream>

using namespace std;

int main()
{
	int limf, lims, sum = 0, res;
	

	cout << "Ingrese el limite inferior: " << endl;
	cin >> limf;
	cout << endl;

	cout << "Ingrese el limite superior: " << endl ;
	cin >> lims;
	cout << endl;
	
	while (limf < lims)
	{
		
		sum = sum + limf;
		limf++;
		
	}

	res = sum + lims;
    
	cout << res;
	
	
	cout << endl;
	

	cout << endl;
	system("pause");
	cout << endl << endl;
}