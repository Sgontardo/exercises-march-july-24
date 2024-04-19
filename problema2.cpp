/*Implementa en C++ un programa (Class) que determine si los delimitadores (,),{,},[,] en
una expresión aritmética (e.j. [(5+x)-(y+z)]) están equilibrados..
• Ejemplo de expresión correcta: ()(()){([()])}
• Ejemplo de expresión incorrecta: ({[])}
Utiliza una pila para implementar la solución. Considera las siguientes pistas:
• Si encontramos un símbolo de apertura [,(,{ debemos apilarla.
• Si encontramos un símbolo de cierre ],},) entonces consultamos el elemento que
hay en la cima de pila. Si son de distinto tipo, podemos afirmar que la expresión
no está balanceada. Si son del mismo tipo, debemos desapilar.
• La expresión estará balanceada si al terminar de leer la expresión la pila está
vacía.
*/

#include <iostream>
#include <stack>
#include <string>
using namespace std;


bool sonDelimitadoresEquilibrados(const  string& expresion) {
     stack<char> pila;

    for (char c : expresion) {
        if (c == '(' || c == '[' || c == '{') {
            // Si encontramos un símbolo de apertura, lo apilamos
            pila.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            // Si encontramos un símbolo de cierre, verificamos con el elemento en la cima de la pila
            if (pila.empty()) {
                return false; // Expresión desequilibrada
            }

            char tope = pila.top();
            pila.pop();

            // Verificamos si los delimitadores coinciden
            if ((c == ')' && tope != '(') ||
                (c == ']' && tope != '[') ||
                (c == '}' && tope != '{')) {
                return false; // Expresión desequilibrada
            }
        }
    }

    // La expresión está balanceada si la pila está vacía al final
    return pila.empty();
}

int main() {
     string expresion;
     
     cout << " Ingresa Expresion matemática a evaluar: " <<  endl;
    cin >> expresion;
    if (sonDelimitadoresEquilibrados(expresion)) {
         cout << "La expresión  está balanceada." <<  endl;
    } else {
         cout << "La expresión NO está balanceada." <<  endl;
    }


    return 0;
}
