
#include <iostream>

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
};

class BinarySearchTree {
private:
    TreeNode* root;

    // Función auxiliar para insertar un nodo en el árbol
    TreeNode* insertNode(TreeNode* node, int value) {
        if (node == nullptr) {
            return new TreeNode{value, nullptr, nullptr};
        }
        if (value < node->data) {
            node->left = insertNode(node->left, value);
        } else if (value > node->data) {
            node->right = insertNode(node->right, value);
        }
        return node;
    }

    // Función auxiliar para eliminar un nodo del árbol
    TreeNode* deleteNode(TreeNode* node, int value) {
        if (node == nullptr) {
            return nullptr;
        }
        if (value < node->data) {
            node->left = deleteNode(node->left, value);
        } else if (value > node->data) {
            node->right = deleteNode(node->right, value);
        } else {
            if (node->left == nullptr) {
                TreeNode* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {
                TreeNode* temp = node->left;
                delete node;
                return temp;
            }
            TreeNode* minRight = findMin(node->right);
            node->data = minRight->data;
            node->right = deleteNode(node->right, minRight->data);
        }
        return node;
    }

    // Función auxiliar para encontrar el nodo con el valor mínimo
    TreeNode* findMin(TreeNode* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }

    // Función auxiliar para recorrer el árbol en orden
    void inOrderTraversal(TreeNode* node) {
        if (node != nullptr) {
            inOrderTraversal(node->left);
            std::cout << node->data << " ";
            inOrderTraversal(node->right);
        }
    }

public:
    BinarySearchTree() : root(nullptr) {}

    // Insertar un valor en el árbol
    void insert(int value) {
        root = insertNode(root, value);
    }

    // Eliminar un valor del árbol
    void remove(int value) {
        root = deleteNode(root, value);
    }

    // Recorrer el árbol en orden
    void inOrder() {
        inOrderTraversal(root);
        std::cout << std::endl;
    }
};

int main() {
    BinarySearchTree bst;
    int choice, value;

    do {
        std::cout << "Menú:" << std::endl;
        std::cout << "1. Insertar nodo" << std::endl;
        std::cout << "2. Eliminar nodo" << std::endl;
        std::cout << "3. Recorrer en orden" << std::endl;
        std::cout << "0. Salir" << std::endl;
        std::cout << "Ingrese su elección: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Ingrese el valor a insertar: ";
                std::cin >> value;
                bst.insert(value);
                break;
            case 2:
                std::cout << "Ingrese el valor a eliminar: ";
                std::cin >> value;
                bst.remove(value);
                break;
            case 3:
                std::cout << "Recorrido en orden: ";
                bst.inOrder();
                break;
            case 0:
                std::cout << "Saliendo del programa." << std::endl;
                break;
            default:
                std::cout << "Opción no válida. Intente de nuevo." << std::endl;
        }
    } while (choice != 0);

    return 0;
}