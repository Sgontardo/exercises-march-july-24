/*Problema 1
–
Inversa de una palabra.
Implementa una clase en C++ que tenga un método que reciba una palabra y devuelva
su inversa (por ejemplo: ROMA-> AMOR). Utiliza una pila de caracteres para
implementar la solución.*/
#include <iostream>
#include <stack>
#include <string>
using namespace std;

class InversorPalabra {


public:
    string invertirPalabra(const std::string& palabra) {
        stack<char> pila;
        for (char c : palabra) {
            pila.push(c);
        }

        string inversa;
        while (!pila.empty()) {
            inversa += pila.top();
            pila.pop();
        }

        return inversa;
    }
};

int main() {
    InversorPalabra inversor;
    string palabra  ;
    string inversa ;

    cout << " Ingresa Palabra original: " <<  endl;
    cin >> palabra;
    inversa = inversor.invertirPalabra(palabra);
    cout << "Palabra invertida: " << inversa << endl;

    return 0;
}
