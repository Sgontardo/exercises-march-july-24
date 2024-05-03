#include <iostream>
using namespace std;

// Definición de la estructura de nodo
struct Node {
    int data;
    Node* next;
};

// Definición de la clase Cola
class Cola {
private:
    Node* front;
    Node* rear;

public:
    // Constructor
    Cola() {
        front = nullptr;
        rear = nullptr;
    }

    // Función para verificar si la cola está vacía
    bool isEmpty() {
        return (front == nullptr);
    }

    // Función para insertar un elemento en la cola
    void enqueue(int value) {
        Node* newNode = new Node;
        newNode->data = value;
        newNode->next = nullptr;

        if (isEmpty()) {
            front = newNode;
            rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }

        cout << "Elemento insertado: " << value << endl;
    }

    // Función para eliminar un elemento de la cola
    void dequeue() {
        if (isEmpty()) {
            cout << "La cola está vacía." << endl;
        } else {
            Node* temp = front;
            cout << "Elemento eliminado: " << front->data << endl;
            front = front->next;
            delete temp;
        }
    }

    // Función para mostrar los elementos de la cola
    void display() {
        if (isEmpty()) {
            cout << "La cola está vacía." << endl;
        } else {
            Node* temp = front;
            cout << "Elementos en la cola: ";
            while (temp != nullptr) {
                cout << temp->data << " ";
                temp = temp->next;
            }
            cout << endl;
        }
    }
};

int main() {
    Cola cola;

    cola.enqueue(10);
    cola.enqueue(20);
    cola.enqueue(30);
    cola.display();

    cola.dequeue();
    cola.display();

    return 0;
}