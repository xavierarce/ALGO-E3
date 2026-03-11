from tree_api import BinaryTree
from linear_api import Stack, Queue, LinkedList
from matrix_api import (
    create_matrix_5x4,
    create_matrix,
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    calculate_matrix_operation,
)

def test_trees():
    print("\n--- TEST API ARBRES ---")
    tree = BinaryTree.create_with_n_nodes([50, 30, 70, 20, 40, 15, 25])
    
    print("Infixe (trié) :", tree.inorder_traversal())
    print("Préfixe :      ", tree.preorder_traversal())
    print("Postfixe :     ", tree.postorder_traversal())
    print("Largeur (BFS) :", tree.level_order_traversal())


def test_linear_structures():
    print("\n--- TEST API LINÉAIRE ---")

    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Pile vide ?", stack.is_empty())
    print("Dépiler :", stack.pop())
    print("Rechercher 1 dans pile :", stack.search(1))

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print("File vide ?", queue.is_empty())
    print("Retirer :", queue.dequeue())
    print("Rechercher 20 dans file :", queue.search(20))

    linked = LinkedList()
    linked.insert("A")
    linked.insert("B")
    linked.insert("C")
    print("Liste chaînée :", linked.to_list())
    print("Rechercher B :", linked.search("B"))
    linked.delete("B")
    print("Après suppression de B :", linked.to_list())


def test_matrices():
    print("\n--- TEST API MATRICES ---")

    matrix_5x4 = create_matrix_5x4(1)
    print("Matrice 5x4 :", matrix_5x4)

    a = create_matrix(2, 2)
    b = create_matrix(2, 2)
    a[0][0], a[0][1], a[1][0], a[1][1] = 1, 2, 3, 4
    b[0][0], b[0][1], b[1][0], b[1][1] = 5, 6, 7, 8

    print("Addition :", add_matrices(a, b))
    print("Soustraction :", subtract_matrices(a, b))
    print("Multiplication :", multiply_matrices(a, b))
    print("Calcul standard (+) :", calculate_matrix_operation("+", a, b))

if __name__ == "__main__":
    test_trees()
    test_linear_structures()
    test_matrices()