# 📘 Projet Algorithmique Avancée - ESGI (2025-2026)

Ce projet consiste à développer une bibliothèque (API) complète en Python couvrant les structures de données fondamentales : Arbres Binaires, Matrices, et Structures Linéaires.

---

## 🚀 Plan de Développement

### Étape 1 : Structures Linéaires (Piles, Files, Listes)
* **Pile (LIFO) :** Implémentation des fonctions `est_vide`, `empiler`, `depiler`.
* **File (FIFO) :** Implémentation des fonctions `file_vide`, `ajouter`, `retirer`.
* **Liste Chaînée :** Fonctions d'insertion, de suppression et de recherche universelle.
* **Recherche :** Algorithme de recherche d'un élément commun aux trois structures (Pile, File, Liste).

### Étape 2 : API Arbres Binaires
* **Création :** Fonction de génération automatique d'un arbre à n sommets.
* **Parcours en Profondeur (DFS) :**
    * `Parcours Préfixe` (Racine -> Gauche -> Droite)
    * `Parcours Infixe` (Gauche -> Racine -> Droite)
    * `Parcours Postfixe` (Gauche -> Droite -> Racine)
* **Parcours en Largeur (BFS) :** Exploration par niveau en utilisant une file.
* **Modification :** Fonctions d'insertion de feuilles et de branches entières.

### Étape 3 : API Manipulation de Matrices
* **Génération :** Fonctions pour créer des matrices 5x4 et n x m.
* **Opérations Mathématiques :**
    * Addition et Soustraction de matrices compatibles.
    * Multiplication matricielle.
* **Fonction Standard de Calcul :** Interface unique pour les opérations (+, -, x, /).
    * *Note : Gestion de la division par zéro (si divisé par 0, le résultat est forcé à 1).*

### Étape 4 : Tests et Validation
* **Script de test (main.py) :** Validation de chaque fonction de l'API avec des jeux de données concrets.
* **Documentation :** Commentaires explicatifs pour chaque algorithme selon les standards Python.
* **Soutenance :** Préparation du support de présentation (15 min) et démonstration du code.

---

## 🛠️ Installation et Utilisation

1. **Cloner le projet :**
   ```bash
   git clone [https://github.com/xavierarce/ALGO-E3.git](https://github.com/xavierarce/ALGO-E3.git)
   ```
2. **Créer l'environnement virtuel : :**
   ```bash
    # Sur Mac
    python3 -m venv algo_env
    source algo_env/bin/activate

    # Sur Windows
    python -m venv algo_env
    .\algo_env\Scripts\activate
  ```
3. **Lancer les tests :**
   ```bash
    python main.py
    ```

