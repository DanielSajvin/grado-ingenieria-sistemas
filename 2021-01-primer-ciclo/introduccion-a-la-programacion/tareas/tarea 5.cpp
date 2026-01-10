#include <iostream>
#include <windows.h>
#include <time.h>

using namespace std;

void gotoxy(int x, int y)
{
	HANDLE hcon;
	hcon = GetStdHandle(STD_OUTPUT_HANDLE);
	COORD dwPos;
	dwPos.X = x;
	dwPos.Y = y;
	SetConsoleCursorPosition(hcon, dwPos);
}

int main()
{
	int value[5], temp;
	int v = 0;

	srand(time(NULL));
	cout << "Numeros aleatorios: " << endl;
	for (int i = 0; i <= 5; i++)
	{
		value[i] = rand() % 7;
		cout << value[i] << ", ";
	}
	for (v = 0; v <= 6; v++)
	{
		for (int l = v + 1; l <= 6; l++)
		{
			if (value[v] > value[l])
			{
				temp = value[v];
				value[v] = value[l];
				value[l] = temp;
			}
		}
	}
	cout << endl << "Numeros aleatorios ordenados: " << endl;
	for (int i = 0; i <= 5; i++)
	{
		cout << value[i] << ", ";
	}

	cout << endl << endl;
	system("pause");
}
