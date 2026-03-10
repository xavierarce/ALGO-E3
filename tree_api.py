# tree_api.py

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
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