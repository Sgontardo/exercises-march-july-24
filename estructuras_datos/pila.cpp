#include <iostream>
#include <stack>

int main() {
    std::stack<int> pila;

    // Agregar elementos a la pila
    pila.push(10);
    pila.push(20);
    pila.push(30);

    // Obtener el tamaño de la pila
    std::cout << "Tamaño de la pila: " << pila.size() << std::endl;

    // Acceder al elemento en la parte superior de la pila
    std::cout << "Elemento en la parte superior de la pila: " << pila.top() << std::endl;

    // Eliminar el elemento en la parte superior de la pila
    pila.pop();

    // Verificar si la pila está vacía
    if (pila.empty()) {
        std::cout << "La pila está vacía" << std::endl;
    } else {
        std::cout << "La pila no está vacía" << std::endl;
    }

    return 0;
}