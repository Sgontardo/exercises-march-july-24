// Integrantes = Sergio Gontardo y Leonardo Chacon
#include <iostream>
#include <string>

using namespace std;

int main() {
    int intentos = 6;
    string palabra = "mariposa";
    string aux = "--------";
    cout << "Adivine la palabra escondida (tiene 6 intentos)" << endl;
    cout << aux << endl;

    int len = palabra.length();
    while (intentos != 0) {
        bool encontre=false;
        cout << "Ingrese una letra: "<<endl;
        char letra;
        cin >> letra;
        for (int i = 0; i < len; i++) {
            if(letra == palabra[i]){
                aux[i]= palabra[i];
                cout<<aux<<endl;
                encontre = true;
            }
        }
            if (!encontre) {
            intentos = intentos - 1;
            cout << "Perdiste un intento. Intentos restantes: " << intentos << endl;
        }
            if(aux == palabra){
            cout<<"Adivinaste la palabra";
            return 0;
        }
    }
    cout<<"Perdiste, no adivinaste la palabra; intenta otra vez ;)";
    return 0;
}