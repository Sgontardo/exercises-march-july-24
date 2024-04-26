#include <iostream>
#include <vector>
using namespace std;

// Definición de la estructura para estudiantes
struct Student {
    string name;
    int age;
    int id;
};

// Función para comparar estudiantes por nombre
bool compareByName(const Student& s1, const Student& s2) {
    return s1.name < s2.name;
}

// Función para comparar estudiantes por edad
bool compareByAge(const Student& s1, const Student& s2) {
    return s1.age < s2.age;
}

// Función para comparar estudiantes por identificación
bool compareById(const Student& s1, const Student& s2) {
    return s1.id < s2.id;
}

// Función para ordenar el vector utilizando el método de la burbuja
void bubbleSort(vector<Student>& students, bool (*compareFunc)(const Student&, const Student&)) {
    int n = students.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (compareFunc(students[j], students[j + 1])) {
                // Intercambiar elementos si están en el orden incorrecto
                swap(students[j], students[j + 1]);
            }
        }
    }
}

int main() {
    vector<Student> students;

    // Ingresar datos de estudiantes (puedes hacerlo mediante un bucle)
    students.push_back({"Alice", 20, 101});
    students.push_back({"Bob", 22, 102});
    students.push_back({"Charlie", 19, 103});

    // Ordenar por nombre utilizando el método de la burbuja
    bubbleSort(students, compareByName);
    cout << "Estudiantes ordenados por nombre:" << endl;
    for (const auto& student : students) {
        cout << student.name << " (" << student.age << " años, ID: " << student.id << ")" << endl;
    }

    // Ordenar por edad utilizando el método de la burbuja
    bubbleSort(students, compareByAge);
    cout << "\nEstudiantes ordenados por edad:" << endl;
    for (const auto& student : students) {
        cout << student.name << " (" << student.age << " años, ID: " << student.id << ")" << endl;
    }

    // Ordenar por identificación utilizando el método de la burbuja
    bubbleSort(students, compareById);
    cout << "\nEstudiantes ordenados por identificación:" << endl;
    for (const auto& student : students) {
        cout << student.name << " (" << student.age << " años, ID: " << student.id << ")" << endl;
    }

    return 0;
}
