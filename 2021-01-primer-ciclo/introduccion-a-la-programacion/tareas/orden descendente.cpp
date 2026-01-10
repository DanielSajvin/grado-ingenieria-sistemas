#include <iostream>

using namespace std;

int main()
{
	int i = 0, li = 200;

	while (i < 200)
	{
		cout << li << ", ";
		li = li - 5;
		if (li == 0)
		{
			break;
		}
		i++;
	}

	cout << endl;
	system("pause");
	cout << endl;
	//////////////////
	

}