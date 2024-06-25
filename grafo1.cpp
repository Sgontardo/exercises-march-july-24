#include <iostream>

using namespace std;

struct Nodo {
    int dato;
    Nodo* siguiente;
    Nodo* anterior;
    Nodo* arriba;
    Nodo* abajo;
    int peso;
};

void agregarNodo(Nodo* &nodo, int dato) {
    if (nodo == nullptr) {
        nodo = new Nodo;
        nodo->dato = dato;
        nodo->siguiente = nullptr;
        nodo->anterior = nullptr;
        nodo->arriba = nullptr;
        nodo->abajo = nullptr;
    } else {
        agregarNodo(nodo->siguiente, dato);
    }
}

void agregarArista(Nodo* &nodo1, Nodo* &nodo2, int peso) {
    nodo1->peso = peso;
    nodo2->peso = peso;
    nodo1->siguiente = nodo2;
    nodo2->anterior = nodo1;
}

void imprimirGrafo(Nodo* nodo) {
    if (nodo != nullptr) {
        cout << nodo->dato << " ";
        imprimirGrafo(nodo->siguiente);
    } else {
        cout << endl;
    }
}

void matrizAdyacencia(Nodo* nodo) {
    if (nodo != nullptr) {
        if (nodo->siguiente != nullptr) {
            cout << "1 ";
        } else {
            cout << "0 ";
        }
        matrizAdyacencia(nodo->siguiente);
    } else {
        cout << endl;
    }
}

void imprimirMatrizAdyacencia(Nodo* nodo) {
    if (nodo != nullptr) {
        matrizAdyacencia(nodo);
        imprimirMatrizAdyacencia(nodo->abajo);
    }
}

int main() {
    Nodo* grafo = nullptr;
    agregarNodo(grafo, 1);
    agregarNodo(grafo, 2);
    agregarNodo(grafo, 3);
    agregarNodo(grafo->abajo, 4);
    agregarNodo(grafo->abajo, 5);
    agregarNodo(grafo->abajo, 6);
    agregarNodo(grafo->abajo->siguiente, 7);
    agregarNodo(grafo->abajo->siguiente, 8);
    agregarNodo(grafo->abajo->siguiente, 9);
    agregarNodo(grafo->abajo->siguiente->siguiente, 10);
    agregarNodo(grafo->abajo->siguiente->siguiente, 11);
    agregarNodo(grafo->abajo->siguiente->siguiente, 12);
    agregarNodo(grafo->abajo->abajo, 13);
    agregarNodo(grafo->abajo->abajo, 14);
    agregarNodo(grafo->abajo->abajo, 15);
    agregarNodo(grafo->abajo->abajo->siguiente, 16);
    agregarNodo(grafo->abajo->abajo->siguiente, 17);
    agregarNodo(grafo->abajo->abajo->siguiente, 18);
    agregarNodo(grafo->abajo->abajo->siguiente->siguiente, 19);
    agregarNodo(grafo->abajo->abajo->siguiente->siguiente, 20);
    agregarNodo(grafo->abajo->abajo->siguiente->siguiente, 21);
    agregarNodo(grafo->abajo->abajo->siguiente->siguiente->siguiente, 22);
    agregarNodo(grafo->abajo->abajo->siguiente->siguiente->siguiente, 23);
    agregarNodo(grafo->abajo->abajo->siguiente->siguiente->siguiente, 24);
    agregarNodo(grafo->abajo->abajo->siguiente->siguiente->siguiente->siguiente, 25);

    matrizAdyacencia(grafo);
    imprimirGrafo(grafo);
    imprimirMatrizAdyacencia(grafo);

    return 0;
}
