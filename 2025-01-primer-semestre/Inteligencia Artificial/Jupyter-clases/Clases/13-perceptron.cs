using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Task;

// ejemplo de perceptron para implementar la puerta logica AND
namespace Perceptron
{
    // clase para el bloque de codigo
    class Program
    {
        static void Main(string[] args)
        {
            // conjunto de datos para entrenamiento
            int[,] datos = {{ 1,1,1}, { 1,0,0}, { 0,1,0}, { 0,0,0}};
            // generacion de los valores de peso y umbral 
            Random aleatorio = new Random();
            double[] pesos = {aleatorio.NextDouble(),aleatorio.NextDouble(),aleatorio.NextDouble()};

            // Estapa de aprendizaje 
            bool aprendizaje =  true;

            //salida, variable en funcion de la respuesta, si supera el 0 es 1 y si no es 0
            int salidaInt;
            int epocas = 0;

            while (aprendizaje)
            {
                aprendizaje = false;
                for (int i = 0; i < 4; i++)
                {
                    double salidaDoub = datos[i, 0] * pesos[0] + datos[i, 1] * pesos[1] + pesos[2];
                    if (salidaDoub > 0) salidaInt = 1; else salidaInt = 0;
                    if (salidaInt != datos[i, 2]) {
                        pesos[0] = aleatorio.NextDouble() - aleatorio.NextDouble();
                        pesos[1] = aleatorio.NextDouble() - aleatorio.NextDouble();
                        pesos[2] = aleatorio.NextDouble() - aleatorio.NextDouble();
                        aprendizaje = true;
                    }
                }
                epocas++;
            }
            // finaliza el aprendizaje 
            // verificacion de resulados 
            for (int i = 0; i < 4; i++)
            {
                double salidaDoub = datos[i, 0] * pesos[0] + datos[i, 1] * pesos[1] + pesos[2];
                if(salidaDoub > 0)salidaInt = 1; else salidaInt = 0;
                Console.WriteLine("Entradas: " + datos[i,0].ToString() + " AND " + datos[i,1].ToString() + " = " + datos[i,2].ToString() + " Perceptron: " + salidaInt.ToString());
                
            }
            Console.WriteLine("Epocas: " + epocas.ToString());
            Console.WriteLine("Pesos Utiles: p0= " + pesos[0].ToString() + " p1= "+ pesos[1].ToString() + " Umbral (bias): " + pesos[2].ToString());
            Console.ReadLine();
        }
    }
}