from tree_api import BinaryTree

def test_trees():
    print("\n--- TEST API ARBRES ---")
    tree = BinaryTree()
    for v in [50, 30, 70, 20, 40]:
        tree.insert(v)
    
    print("Infixe (trié) :", tree.inorder_traversal())
    print("Préfixe :      ", tree.preorder_traversal())
    print("Postfixe :     ", tree.postorder_traversal())

if __name__ == "__main__":
    test_trees()