def tri_a_bulles(arr):
    n = len(arr)
    
    # Boucle pour parcourir tous les éléments du tableau
    for i in range(n):
        swapped = False
        
        # La boucle interne compare les éléments adjacents.
        # On va jusqu'à n-i-1 car les i derniers éléments sont déjà à leur place.
        for j in range(0, n - i - 1):
            
            # Si l'élément actuel est plus grand que le suivant, on échange
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # Si aucun échange n'a été fait lors de ce passage, 
        # le tableau est déjà trié. On arrête.
        if not swapped:
            break
        print(arr)
            
    return arr

# --- Exemple d'utilisation ---
ma_liste = [64, 34, 25, 12, 22, 11, 90]
liste_triee = tri_a_bulles(ma_liste)

print("Liste triée :", liste_triee)