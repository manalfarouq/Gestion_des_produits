#  menu file

while True:
    print("\n===== Gestion des Produits =====")
    print("1 -> Ajouter un produit")
    print("2 -> Supprimer un produit")
    print("3 -> Modifier la quantité dun produit")
    print("4 -> Afficher le stock")
    print("5 -> Afficher les statistiques")
    print("6 -> Afficher un graphique")
    print("0 -> Quitter")
    
    choix = input("\nVotre choix : ")
    
    if choix == "1":
        ajouter_produit()
    elif choix == "2":
        supprimer_produit()
    elif choix == "3":
        modifier_quantite()
    elif choix == "4":
        afficher_stock()
    elif choix == "5":
        afficher_statistiques()
    elif choix == "6":
        afficher_graphique()
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, réessayez.")