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
    tree = BinaryTree.create_with_n_nodes([50, 30, 70, 20, 40])
    
    print("Infixe (trié) :", tree.inorder_traversal())
    print("Préfixe :      ", tree.preorder_traversal())
    print("Postfixe :     ", tree.postorder_traversal())
    print("Largeur (BFS) :", tree.level_order_traversal())



def test_linear_structures():
    print("\n--- TEST API LINÉAIRE ---")

    pile = Pile()
    pile.empiler(1)
    pile.empiler(2)
    print("Pile vide ?", pile.pile_vide())
    print("Dépiler :", pile.depiler())
    print("Rechercher 1 dans pile :", pile.rechercher(1))

    file = File()
    file.ajouter(10)
    file.ajouter(20)
    print("File vide ?", file.file_vide())
    print("Retirer :", file.retirer())
    print("Rechercher 20 dans file :", file.rechercher(20))

    liste = ListeChainee()
    liste.inserer("A")
    liste.inserer("B")
    liste.inserer("C")
    print("Liste chaînée :", liste.to_list())
    print("Rechercher B :", liste.rechercher("B"))
    liste.supprimer("B")
    print("Après suppression de B :", liste.to_list())


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