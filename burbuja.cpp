
#include <iostream>
#include <vector>
using namespace std;

// Función para ordenar un vector utilizando el método de la burbuja
void ordenarVector(vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (vec[j] > vec[j + 1]) {
                // Intercambiar elementos si están en el orden incorrecto
                swap(vec[j], vec[j + 1]);
            }
        }
    }
}

int main() {
    vector<int> miVector = {5,15,3, 2, 8, 1}; // Cambia los valores según tus necesidades

    // Mostrar los elementos del vector (sin ordenar)
    cout << "Elementos en el vector (sin ordenar): ";
    for (int elem : miVector) {
        cout << elem << " ";
    }
    cout << endl;

    // Ordenar el vector utilizando el método de la burbuja
    ordenarVector(miVector);

    // Mostrar los elementos del vector (ordenados)
    cout << "Elementos en el vector (ordenados): ";
    for (int elem : miVector) {
        cout << elem << " ";
    }
    cout << endl;

    return 0;
}