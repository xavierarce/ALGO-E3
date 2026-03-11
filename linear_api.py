class Pile:
    def __init__(self):
        self._items = []

    def pile_vide(self):
        """Vérifie si la pile est vide (Pile-vide ?)"""
        return len(self._items) == 0

    def empiler(self, value):
        """Ajoute un élément au sommet de la pile"""
        self._items.append(value)

    def depiler(self):
        """Retire et renvoie l'élément au sommet de la pile"""
        if self.pile_vide():
            raise IndexError("Erreur : Pile vide")
        return self._items.pop()

    def rechercher(self, target):
        """Recherche un élément dans la pile"""
        return target in self._items


class File:
    def __init__(self):
        self._items = []

    def file_vide(self):
        """Vérifie si la file est vide (File vide ?)"""
        return len(self._items) == 0

    def ajouter(self, value):
        """Ajoute un élément à la fin de la file"""
        self._items.append(value)

    def retirer(self):
        """Retire et renvoie le premier élément de la file"""
        if self.file_vide():
            raise IndexError("Erreur : File vide")
        return self._items.pop(0)

    def rechercher(self, target):
        """Recherche un élément dans la file"""
        return target in self._items


class Maillon:
    """Classe représentant un nœud de la liste chaînée"""
    def __init__(self, value):
        self.value = value
        self.next = None


class ListeChainee:
    def __init__(self):
        self.head = None

    def inserer(self, value):
        """Insère un élément à la fin de la liste"""
        nouveau = Maillon(value)
        if self.head is None:
            self.head = nouveau
            return

        courant = self.head
        while courant.next is not None:
            courant = courant.next
        courant.next = nouveau

    def supprimer(self, value):
        """Supprime la première occurrence d'une valeur"""
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        precedent = self.head
        courant = self.head.next
        while courant is not None:
            if courant.value == value:
                precedent.next = courant.next
                return True
            precedent = courant
            courant = courant.next
        return False

    def rechercher(self, target):
        """Recherche un élément dans la liste chaînée"""
        courant = self.head
        while courant is not None:
            if courant.value == target:
                return True
            courant = courant.next
        return False

    def to_list(self):
        """Convertit la liste chaînée en liste Python classique pour l'affichage"""
        values = []
        courant = self.head
        while courant is not None:
            values.append(courant.value)
            courant = courant.next
        return values
