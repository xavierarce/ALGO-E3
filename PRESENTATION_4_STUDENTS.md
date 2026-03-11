# Répartition de la présentation (4 étudiants)

## Objectif
Proposer une soutenance claire de **15 minutes** en respectant l’ordre du syllabus :
1. API Arbres binaires
2. API Structures linéaires (pile, file, liste chaînée)
3. API Matrices
4. Conclusion / livrables / références

---

## Plan global (15 min)
- **Étudiant 1** : 0:00 → 3:30
- **Étudiant 2** : 3:30 → 7:00
- **Étudiant 3** : 7:00 → 10:30
- **Étudiant 4** : 10:30 → 15:00

---

## Étudiant 1 — Introduction + API Arbres (partie 1)
**Durée : 3 min 30**

### Slides conseillées
1. **Contexte du projet**
   - Année 2025-2026, algorithmique avancée
   - Objectif : définir des API en Python
2. **Structure du dépôt et choix techniques**
   - Fichiers : `tree_api.py`, `linear_api.py`, `matrix_api.py`, `main.py`
   - Pourquoi une API modulaire
3. **Arbres binaires : création + insertion**
   - Création d’un arbre avec n sommets
   - Insertion d’une feuille
   - Insertion d’une branche

### Ce qu’il/elle dit
- Présenter rapidement le besoin du syllabus.
- Expliquer la modélisation `Node` et `BinaryTree`.
- Montrer un exemple de création d’arbre et insertion.

---

## Étudiant 2 — API Arbres (partie 2)
**Durée : 3 min 30**

### Slides conseillées
4. **Parcours en profondeur (DFS)**
   - Préfixe
   - Infixe
   - Postfixe
5. **Parcours en largeur (BFS)**
   - Principe niveau par niveau
   - Utilisation d’une file
6. **Démonstration rapide des sorties**
   - Résultats obtenus dans `main.py`

### Ce qu’il/elle dit
- Expliquer la logique de chaque parcours.
- Justifier l’intérêt de chaque ordre de parcours.
- Faire le lien avec les exigences exactes du sujet.

---

## Étudiant 3 — API Structures linéaires
**Durée : 3 min 30**

### Slides conseillées
7. **Pile (LIFO)**
   - Pile vide ?
   - Empiler
   - Dépiler
8. **File (FIFO)**
   - File vide ?
   - Ajouter
   - Retirer
9. **Liste chaînée + recherche / insertion / suppression**
   - Recherche dans pile/file/liste
   - Cas d’usage simples

### Ce qu’il/elle dit
- Différencier LIFO et FIFO.
- Expliquer la liste chaînée et ses opérations de base.
- Montrer une mini démo de recherche/insertion/suppression.

---

## Étudiant 4 — API Matrices + Conclusion
**Durée : 4 min 30**

### Slides conseillées
10. **Création de matrices**
    - Fonction 5x4
    - Fonction n x m
11. **Opérations matricielles**
    - Addition, soustraction, multiplication
    - Compatibilité des dimensions
12. **Fonction standard d’opération**
    - Paramètre opérateur : `+`, `-`, `x`, `/`
    - Règle demandée : division par zéro => résultat `1`
13. **Conclusion + livrables + références**
    - Travail écrit
    - Démo code
    - Références bibliographiques

### Ce qu’il/elle dit
- Montrer que toutes les exigences matrices sont couvertes.
- Conclure sur la qualité de l’API et les tests.
- Ouvrir sur améliorations possibles (validation, performance, tests avancés).

---

## Checklist finale avant soutenance
- Vérifier que chaque étudiant respecte son temps.
- Faire une répétition avec chronomètre.
- Préparer 1 slide de secours avec captures de sortie console.
- Prévoir qui répond aux questions techniques (arbres / linéaires / matrices).
- Vérifier cohérence entre PowerPoint, code, et travail écrit.
