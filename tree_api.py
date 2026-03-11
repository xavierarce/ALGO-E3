# tree_api.py

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    @classmethod
    def create_with_n_nodes(cls, values):
        """Crée un arbre binaire de recherche à partir d'une séquence de valeurs."""
        tree = cls()
        for value in values:
            tree.insert(value)
        return tree
    
    def insert(self, value):
        """Insère une valeur (Arbre Binaire de Recherche)"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # --- LES PARCOURS (Demandés par le syllabus) ---

    def inorder_traversal(self, node=None, res=None):
        """Parcours INFIXE : renvoie une liste [gauche, racine, droite]"""
        if res is None: res = []
        if node is None: node = self.root
        
        if node:
            if node.left: self.inorder_traversal(node.left, res)
            res.append(node.value)
            if node.right: self.inorder_traversal(node.right, res)
        return res

    def preorder_traversal(self, node=None, res=None):
        """Parcours PRÉFIXE : renvoie une liste [racine, gauche, droite]"""
        if res is None: res = []
        if node is None: node = self.root
        
        if node:
            res.append(node.value)
            if node.left: self.preorder_traversal(node.left, res)
            if node.right: self.preorder_traversal(node.right, res)
        return res

    def postorder_traversal(self, node=None, res=None):
        """Parcours POSTFIXE : renvoie une liste [gauche, droite, racine]"""
        if res is None: res = []
        if node is None: node = self.root
        
        if node:
            if node.left: self.postorder_traversal(node.left, res)
            if node.right: self.postorder_traversal(node.right, res)
            res.append(node.value)
        return res

    def level_order_traversal(self):
        """Parcours en largeur (BFS)."""
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return result

    def insert_leaf(self, value):
        """Insertion d'une feuille (alias de l'insertion standard BST)."""
        self.insert(value)

    def insert_branch(self, parent_value, branch_values, side="left"):
        """Insère une branche sous un parent existant, côté gauche ou droit."""
        parent = self._find(self.root, parent_value)
        if parent is None:
            raise ValueError("Parent introuvable dans l'arbre")

        if side not in ("left", "right"):
            raise ValueError("Le paramètre side doit valoir 'left' ou 'right'")

        if not branch_values:
            return

        branch_root = Node(branch_values[0])
        current = branch_root
        for value in branch_values[1:]:
            current.left = Node(value)
            current = current.left

        if side == "left":
            if parent.left is not None:
                raise ValueError("Le parent possède déjà un enfant gauche")
            parent.left = branch_root
        else:
            if parent.right is not None:
                raise ValueError("Le parent possède déjà un enfant droit")
            parent.right = branch_root

    def _find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return self._find(node.left, value)
        return self._find(node.right, value)