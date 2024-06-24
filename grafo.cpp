#include <iostream>
#include <vector>
#include <string>
#include <cmath>

const int NUM_CITIES = 25;

// Estructura para representar una ciudad
struct City {
    std::string name;
    double latitude; // Latitud en grados decimales
    double longitude; // Longitud en grados decimales
};

// Calcula la distancia entre dos ciudades utilizando la fórmula de Haversine
double calculateDistance(const City& city1, const City& city2) {
    const double R = 6371.0; // Radio de la Tierra en kilómetros

    double lat1_rad = city1.latitude * M_PI / 180.0;
    double lon1_rad = city1.longitude * M_PI / 180.0;
    double lat2_rad = city2.latitude * M_PI / 180.0;
    double lon2_rad = city2.longitude * M_PI / 180.0;

    double dlon = lon2_rad - lon1_rad;
    double dlat = lat2_rad - lat1_rad;

    double a = std::sin(dlat / 2.0) * std::sin(dlat / 2.0) +
               std::cos(lat1_rad) * std::cos(lat2_rad) *
               std::sin(dlon / 2.0) * std::sin(dlon / 2.0);

    double c = 2.0 * std::atan2(std::sqrt(a), std::sqrt(1.0 - a));

    return R * c;
}

int main() {
    std::vector<City> cities(NUM_CITIES);

    // Ciudades con sus nombres, latitudes y longitudes
    cities[0] = { "Caracas", 10.4880, -66.8792 };
    cities[1] = { "Maracaibo", 10.6480, -71.6127 };
    cities[2] = { "Valencia", 10.1620, -68.0073 };
    cities[3] = { "Barinas", 8.62261,   -70.20749 };
    cities[4] = { "Turmero",10.22856,   -67.47421 };
    cities[5] = { "San Juan de los Morros", 9.74569,   -63.18323 };
    cities[6] = { "Porlamar", 10.96389,   -63.8491 };
    cities[7] = { "La Victoria", 10.22376,   -67.33101 };
    cities[8] = { "Charallave", 10.16245,   -66.88248 };
    cities[9] = { "Cumaná", 10.46417,   -64.1775 };
    cities[10] = { "Tinaquillo", 9.91833,   -68.30444 };
    cities[11] = { "Cagua", 10.18667,   -67.45944 };
    cities[12] = { "Anaco", 9.43889,   -64.47278 };
    cities[13] = { "Calabozo", 8.92417,   -67.42944 };
    cities[14] = { "San Carlos", 9.66306,   -68.58444 };
    cities[15] = { "San Felipe", 10.33918,   -68.74259 };
    cities[16] = { "Guanare", 9.04183,   -69.74215 };
    cities[17] = { "Carúpano", 10.66706,   -63.2585 };
    cities[18] = { "Araure", 9.56667,   -69.21667 };
    cities[19] = { "Güigüe", 10.08556,   -67.78167 };
    cities[20] = { "Ejido", 8.55194,   -71.23722 };
    cities[21] = { "Mariara", 10.29833,   -67.71667 };
    cities[22] = { "Coro", 11.40402,   -69.6734 };
    // ... Agrega las otras ciudades con sus datos

    // Crear una matriz de adyacencia para almacenar las distancias entre ciudades
    std::vector<std::vector<double>> adjacencyMatrix(NUM_CITIES, std::vector<double>(NUM_CITIES, 0.0));

    // Calcular las distancias y llenar la matriz de adyacencia
    for (int i = 0; i < NUM_CITIES; ++i) {
        for (int j = i + 1; j < NUM_CITIES; ++j) {
            double distance = calculateDistance(cities[i], cities[j]);
            adjacencyMatrix[i][j] = distance;
            adjacencyMatrix[j][i] = distance; // La matriz es simétrica
        }
    }

    // Imprimir la matriz de adyacencia (puedes personalizar el formato)
    for (const auto& row : adjacencyMatrix) {
        for (double distance : row) {
            std::cout << distance << "\t";
        }
        std::cout << std::endl;
    }

    return 0;
}