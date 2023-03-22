import matplotlib.pyplot as plt
import time

# le système de monnaie disponible
valeurs = [1, 2, 5, 10, 13, 20, 50, 100, 200]
 
def rendu_de_monnaie(a_rendre):
    liste = []
   
 
    # indice « tout à droite »
    indice = len(valeurs) - 1
 
    while a_rendre > 0: # on sort quand tout payé
        piece = valeurs[indice]
        # Soit la pièce est trop grande
        if piece > a_rendre:
            # on regardera une piece plus petite
            indice -= 1
        # soit on la rend (on rembourse)
        else:
            # on l'ajoute à la liste
            liste.append(piece)
            # on la soustrait de la somme à rendre
            a_rendre -= piece
    # on renvoie la liste
    return liste

def rendu_de_monnaie_rec(a_rendre):
    if a_rendre ==0:
        return []
    for i in reversed(range(len(valeurs))):
        piece = valeurs[i]
        if piece <= a_rendre:
            return [piece] + rendu_de_monnaie_rec(a_rendre-piece)

 
X = [i for i in range(10000)]
times = []

plt.xlabel("Value")
plt.ylabel("Time Complexity")

# Affichage des pièces et billets à rendre
for x in X:
    t1 = time.process_time()
    liste_de_pieces = rendu_de_monnaie(x)
    t2 = time.process_time()
    #print(f"Temps d'exécution: {(t2-t1):.4f}s")
    times.append(t2-t1)

# print(times)
plt.plot(X, times, label="rendu_glouton")

times=[]
for x in X:
    t1 =time.process_time()
    liste_de_pieces = rendu_de_monnaie_rec(x)
    t2 = time.process_time()
    # print(f"Temps d'exécution: {(t2-t1):.4f}s")
    times.append(t2-t1)

plt.plot(X, times, label="rendu_glouton_rec")

plt.grid()
plt.legend()
plt.show()

# result=rendu_de_monnaie(180)
# print(result)
# result=rendu_de_monnaie_rec(180)
# print(result)