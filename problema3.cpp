/*Implementa un programa	 para	 gestionar	 una	 impresora	 online
    La	 impresora puede	 recibir	 peticiones	 desde	 diferentes	 ordeadores.
    Las	 peticiones	 serán	impresas	por	orden	de	llegada.
    Cada	petición	incluye	la	siguiente	información:
        id	 (String)	 de	 la	 máquina	 que	 solicita	 la	 impresión	 (por	 ejemplo,	 “I3493”) y	 el
nombre	 del	 fichero	 a	 imprimir	 (por	 ejemplo,	 file1.pdf).

    El	 programa	 debe	implementar	los	siguientes	métodos:
        • addRequest:	 toma	 una	 petición	 como	 entrada	 y	 la	 añade	 al	 conjunto	 de
peticiones.
        • printWork:	coge	la	primera	petición	y	muestra	sus	datos	(id	y	nombre	del
ficheor)	 por	 consola	 (únicamente	 simula	 la	 impresión	 de	 la	 petición). La
petición	debe	ser	eliminada	del	conjunto	de	peticiones.
        • getNumRequest():	devuelve	el	número	total	de	peticiones.
        • showAll():	muestra	todas	las	peticiones	que	no	han	sido	impresas.
        • printAll():	 imprime	 todas	 las	 peticiones.	 Después	 de	 procesar	 la	 petición,
está	debe	ser	eliminada.
        • Escribe	 un	método	main	 que	incluya	 las	 llamadas	 necesarias	 para	 validar
todos	los	métodos	descritos	anteriormente.	*/


#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Impresion {
     string id;
     string nombreFichero;
};

class ImpresoraOnline {
private:
     vector<Impresion> peticiones;

public:
    void addRequest(const  string& id, const  string& nombreFichero) {
        peticiones.push_back({id, nombreFichero});
    }

    void printWork() {
        if (!peticiones.empty()) {
            Impresion primeraPeticion = peticiones.front();
             cout << "Imprimiendo petición:" <<  endl;
             cout << "ID: " << primeraPeticion.id << ", Fichero: " << primeraPeticion.nombreFichero <<  endl;
            peticiones.erase(peticiones.begin());
        } else {
             cout << "No hay peticiones pendientes." <<  endl;
        }
    }

    int getNumRequest() const {
        return peticiones.size();
    }

    void showAll() const {
         cout << "Peticiones pendientes:" <<  endl;
        for (const Impresion& peticion : peticiones) {
             cout << "ID: " << peticion.id << ", Fichero: " << peticion.nombreFichero <<  endl;
        }
    }

    void printAll() {
         cout << "Imprimiendo todas las peticiones:" <<  endl;
        while (!peticiones.empty()) {
            Impresion peticion = peticiones.front();
             cout << "ID: " << peticion.id << ", Fichero: " << peticion.nombreFichero <<  endl;
            peticiones.erase(peticiones.begin());
        }
    }
};

int main() {
    ImpresoraOnline impresora;

    // Ejemplo de uso
    impresora.addRequest("I3493", "file1.pdf");
    impresora.addRequest("A1234", "reporte.docx");

    impresora.printWork(); // Imprime la primera petición
    impresora.showAll();   // Muestra las peticiones pendientes
    impresora.printAll();  // Imprime todas las peticiones

    return 0;
}
