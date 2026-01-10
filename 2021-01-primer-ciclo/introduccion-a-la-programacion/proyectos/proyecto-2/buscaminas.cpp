#include <iostream>
#include <vector> //Esta libreria puede manejar arreglos con la capacidad de manejar su tamaño automaticamente
#include<time.h>

using namespace std;

const int principiante = 0; // valores constante del nivel fácil
const int intermedio = 1; // valores constante del nivel intermedio
const int avanzado = 2; // valores contante del nivel avanzado
const int ladomaximo = 30; // Lados máximos del tablero

int nfilas;
int ncolumnas;
int minas;

// Está función controla la dificultad del juego, ya sea fácil, intermedio o dificil
void eligeniveldificultad() 
{
    int nivel;

    cout << endl;
    cout << "\t\t\t\t *******B I E N V E N I D O S   A L   B U S C A M I N A S*******" << endl;
    cout << endl;
    cout << "\tEl juego consiste en despejar todas las casillas de una pantalla que no oculten una mina." << endl<<endl;
    cout << "\t***** R E G L A S *****" << endl<< endl;
    cout << "\tAlgunas casillas tienen un número, el cual indica la cantidad de minas que hay en las casillas" << endl;
    cout << "\tcircundantes. Así, si una casilla tiene el número 3, significa que de las ocho casillas que hay" << endl;
    cout << "\talrededor (si no es en una esquina o borde) hay 3 con minas y 5 sin minas. Si se descubre una" << endl;
    cout << "\tcasilla sin número indica que ninguna de las casillas vecinas tiene mina y éstas se descubren automáticamente." << endl;
    cout << "\tSi se descubre una casilla con una mina se pierde la partida." << endl;
    cout << "\tSe puede poner una marca en las casillas que el jugador piensa que hay minas para ayudar a descubrir las que están cerca." << endl << endl;
    cout << "\t***** N I V E L E S *****" << endl;
    cout << "\tElija que nivel desea jugar: \n\n" << endl;
    cout << "Presione 0 para el nivel Principiante " << endl;
    cout << "Presione 1 para el nivel Intermedio " << endl;
    cout << "Presione 2 para el nivel Avanzado   " << endl;

    cin >> nivel;

    if (nivel == principiante)
    {
        nfilas = 9;
        ncolumnas = 9;
        minas = 10;
    }

    if (nivel == intermedio)
    {
        nfilas = 16;
        ncolumnas = 16;
        minas = 40;
    }

    if (nivel == avanzado)
    {
        nfilas = 16;
        ncolumnas = 30;
        minas = 99;
    }

    return;
}

// Esta función lo que hace es limpiar el tablero del juego
void limpiartablero(char minatablero[][ladomaximo], char tablerojuego[][ladomaximo]) 
{
    for (int i = 0; i < nfilas; i++)
        for (int j = 0; j < ncolumnas; j++)
            tablerojuego[i][j] = minatablero[i][j] = '.';
    return;
}

// Está función tiene como finalidad colocar las minas en el juego de forma aleatoria, colocar minas en el tablero
void colocarminas(char minatablero[][ladomaximo], int minas)
{
    int colocar = 0;
    while (colocar < minas)
    {
        int aleatorio = rand() % (nfilas * ncolumnas);
        int fila = aleatorio / ncolumnas;
        int columna = aleatorio % nfilas;
        if (minatablero[fila][columna] == '#') continue; 
        minatablero[fila][columna] = '#';
        colocar++;
    }
    return;
}

// Reemplaza la mina en una fila o columna y luego la coloca en un espacio vacío, reemplazar las minas o mas bien ocultarlas
void reemplazarmina(int fila, int columna, char minatablero[][ladomaximo])
{
    colocarminas(minatablero, 1);  // Agrega una nueva mina
    minatablero[fila][columna] = '.'; // Aquí remueve la fila y columna vieja o antigua
    return;
}

char indexToChar(int index)
{
    if (index < 10)
        return index + '0';
    else
        return 'a' + (index - 10);
}

int charToIndex(char ch) 
{
    if (ch <= '9')
        return ch - '0';
    else
        return (ch - 'a') + 10;
}

//Está función se encarga de la visualización del tablero
void tablerovisible(char tablerojuego[][ladomaximo]) 
{
    // Acá se imprime la linea superior
    cout << "    ";
    for (int i = 0; i < ncolumnas; i++)
        cout << indexToChar(i) << ' ';
    cout << endl << endl;

    // Se imprimen las filas
    for (int i = 0; i < nfilas; i++) 
    {
        cout << indexToChar(i) << "   ";
        for (int j = 0; j < ncolumnas; j++)
            cout << tablerojuego[i][j] << " ";
        cout << "  " << indexToChar(i);
        cout << endl;
    }

    // Se imprimen los espacios o separaciones
    cout << endl << "    ";
    for (int i = 0; i < ncolumnas; i++)
        cout << indexToChar(i) << ' ';
    cout << endl;

    return;
}

// valida las columnas y las filas
bool valido(int fila, int columna)
{
    return (fila >= 0) && (fila< nfilas) && (columna >= 0) && (columna < ncolumnas);
}

// valida las minas como #
bool esmina(int fila, int columna, char borde[][ladomaximo])
{
    return (borde[fila][columna] == '#');
}

// Retorna todas las filas y columnas del vector
vector < pair <int, int> > casillasvecinas(int fila, int columna) 
{

    vector < pair <int, int> > vecinas;

    for (int distancia = -1; distancia <= 1; distancia++)
        for (int dy = -1; dy <= 1; dy++)
            if (distancia != 0 || dy != 0)
                if (valido(fila + distancia, columna + dy))
                    vecinas.push_back(make_pair(fila + distancia, columna + dy));

    return vecinas;
}

// Está función se encarga de contar el número de minas en las celdas adyacentes, registra los numeros para que no se repitan en el tablero para evitar confusiones
int contarminascercanas(int fila, int columna, char minatablero[][ladomaximo])
{
    vector < pair <int, int> > vecinas = casillasvecinas(fila, columna);

    int contar = 0;
    for (int i = 0; i < vecinas.size(); i++)
        if (esmina(vecinas[i].first, vecinas[i].second, minatablero))
            contar++;

    return contar;
}

// Funcion es una parte de la funcionalidad del juego
void descubrirtablero(char tablerojuego[][ladomaximo], char minatablero[][ladomaximo], int fila, int columna, int* nmovimiento)
{
    (*nmovimiento)++;
    int contar = contarminascercanas(fila, columna, minatablero);
    tablerojuego[fila][columna] = contar + '0';

    // si el número de celda == 0, enseña todas las celdas vecinas. Muestra celdas cercanas que no tengan minas
    if (contar == 0)
    {
        vector < pair <int, int> > vecinas = casillasvecinas(fila, columna);

        for (int i = 0; i < vecinas.size(); i++)
            if (tablerojuego[vecinas[i].first][vecinas[i].second] == '.')
                descubrirtablero(tablerojuego, minatablero, vecinas[i].first, vecinas[i].second, nmovimiento);
    }

    return;
}

// Está función marca las minas, y tambien nos servira para marcar las banderas , parte de la logica del juego
void marcarminas(char tablerojuego[][ladomaximo], char minatablero[][ladomaximo], bool ganado)
{
    for (int i = 0; i < nfilas; i++) 
    {
        for (int j = 0; j < ncolumnas; j++) 
        {
            if (tablerojuego[i][j] == '.' && minatablero[i][j] == '#')
            {
                if (ganado) 
                {
                    tablerojuego[i][j] = 'F';
                }
                else
                {
                    tablerojuego[i][j] = '#';
                }
            }
        }
    }
}

void jugarbuscaminas() 
{
    // Se inicializa
    char minatablero[ladomaximo][ladomaximo], tablerojuego[ladomaximo][ladomaximo];
    int movimientostotales = nfilas * ncolumnas - minas;
    int banderas = minas;
    limpiartablero(minatablero, tablerojuego);
    colocarminas(minatablero, minas);

    // Comenzamos a jugar
    int movimientos = 0;
    bool gameOver = false;

    while (!gameOver) 
    {
        //Se llama la funcion para marcar los border del tablero 
        tablerovisible(tablerojuego);
        cout << banderas << " banderas a la izquierda " << endl << endl;

        // Se toma la entrada de datos
        char x, y, z;
        cout << "Ingrese su movimiento, ingrese primero el numero de fila y despues el numero de columna ->  ";
        cin >> x >> y >> z;
        cout << endl;

        int fila = charToIndex(x);
        int columna = charToIndex(y);

        if (movimientos == 0)
            if (esmina(fila, columna, minatablero))
                reemplazarmina(fila, columna, minatablero);

        if (z == 's')
        {
            if (tablerojuego[fila][columna] == '.' && minatablero[fila][columna] == '.') 
            {
                descubrirtablero(tablerojuego, minatablero, fila, columna, &movimientos);
                if (movimientos == movimientostotales) 
                {
                    marcarminas(tablerojuego, minatablero, true);
                    tablerovisible(tablerojuego);
                    cout << endl << "\t\t\t\t ¡ ¡ ¡ G A N A S T E ! ! ! :)" << endl;
                    gameOver = true;
                }
            }
            else if (tablerojuego[fila][columna] == '.' && minatablero[fila][columna] == '#')
            {
                // game over
                tablerojuego[fila][columna] = '#';
                marcarminas(tablerojuego, minatablero, false);
                tablerovisible(tablerojuego);
                cout << endl << " \t\t\t\t G A M E   O V E R :(" << endl;
                gameOver = true;
            }

            else 
            {
                // Por si quiere desbloquear una casilla con bandera 
                cout << "\t\t\t MOVIMIENTO ILEGAL";
                if (tablerojuego[fila][columna] == 'F')
                    cout << "Celda ya es una bandera. Utilice f para desactivar la bandera.";
                else
                    cout << "La celda ya es un número.";
                cout << endl;
            }
        }

        if (z == 'f') {
            if (tablerojuego[fila][columna] == '.')
            {
                if (banderas != 0)
                {
                    tablerojuego[fila][columna] = 'F';
                    banderas--;
                }
                else 
                {
                    cout << "\t\t\tMovimiento ilegal. ¡Demasiadas banderas!" << endl;
                }
            }
            else if (tablerojuego[fila][columna] == 'F') 
            {
                
                tablerojuego[fila][columna] = '.';
                banderas++;
            }
            else 
            {
               
                cout << "\t\t\t Movimiento ilegal. La celda es un número. " << endl;
            }
        }
    }

    return;
}

// En la función principal ya llamamos a las funciones para que se ejecute sin ningún prblema
int main() 
{
    srand(time(NULL));
    eligeniveldificultad();
    jugarbuscaminas();
    return 0;
}