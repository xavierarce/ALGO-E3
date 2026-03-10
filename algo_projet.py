# Classe représentant un nœud de l'arbre binaire
class Node:
    def __init__(self, value):
        """Initialise un nœud avec une valeur et deux enfants (gauche et droit)"""
        self.value = value  # Valeur stockée dans le nœud
        self.left = None    # Enfant gauche
        self.right = None   # Enfant droit

# Classe représentant un arbre binaire de recherche
class BinaryTree:
    def __init__(self):
        """Initialise un arbre binaire vide"""
        self.root = None  # La racine de l'arbre
    
    def insert(self, value):
        """
        Insère une nouvelle valeur dans l'arbre binaire
        Args:
            value: La valeur à insérer
        """
        if self.root is None:
            self.root = Node(value)  # Crée la racine si l'arbre est vide
        else:
            self._insert_recursive(self.root, value)  # Appelle la fonction récursive
    
    def _insert_recursive(self, node, value):
        """
        Insère récursivement une valeur en respectant la propriété de l'arbre binaire de recherche
        Args:
            node: Le nœud courant
            value: La valeur à insérer
        """
        if value < node.value:
            # Si la valeur est inférieure, insérer dans le sous-arbre gauche
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            # Sinon, insérer dans le sous-arbre droit
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def inorder_traversal(self, node=None):
        """
        Parcourt l'arbre en ordre infixe (gauche, racine, droit)
        Cela permet d'afficher les valeurs dans l'ordre croissant
        Args:
            node: Le nœud courant (par défaut la racine)
        """
        if node is None:
            node = self.root  # Commence par la racine si aucun nœud n'est spécifié
        if node:
            self.inorder_traversal(node.left)      # Parcourir le sous-arbre gauche
            print(node.value, end=" ")              # Afficher la valeur du nœud courant
            self.inorder_traversal(node.right)      # Parcourir le sous-arbre droit


# Point d'entrée du programme
if __name__ == "__main__":
    # Créer un arbre binaire vide
    tree = BinaryTree()
    
    # Insérer des valeurs dans l'arbre
    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)
    
    # Afficher un parcours en ordre infixe (pour vérifier l'ordre croissant)
    print("Inorder traversal:")
    tree.inorder_traversal()