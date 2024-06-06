
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

    // Función auxiliar para mostrar el árbol
    void showTree(TreeNode* node, int level) {
        if (node != nullptr) {
            showTree(node->right, level + 1);
            for (int i = 0; i < level; ++i) {
                std::cout << "  "; // Espacios para la indentación
            }
            std::cout << node->data << std::endl;
            showTree(node->left, level + 1);
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

    // Mostrar el árbol
    void show() {
        showTree(root, 0);
    }
};

int main() {
    BinarySearchTree bst;
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(40);

    std::cout << "Recorrido en orden: ";
    bst.inOrder();

    std::cout << "Árbol:" << std::endl;
    bst.show();

    return 0;
}
