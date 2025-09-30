from stock import update_product, display_products, ajout_produit, supression_produit
from stats import get_stats
from visualize import display_pie_chart, plot_quantite_par_produit
import pandas as pd

choices = [
    " 1- Ajouter un produit.",
    " 2- Supprimer un produit",
    " 3- Modifier la quantité d’un produit",
    " 4- Afficher le stock",
    " 5- Afficher les statistiques",
    " 6- Afficher Graphique en barres : quantité par produit",
    " 7- Camembert (pie chart) : répartition de la valeur totale du stock par produit",
    " 8- Quitter",
]


def menu():
    while True:
        df = pd.read_csv("data/Products.csv")
        print("-----------Menu-----------")
        for choice in choices:
            print(choice)
        print("--------------------------")

        try:
            choice = int(input("Entre votre choix: ").strip())
            print("\n")
        except ValueError:
            print("Merci d'entre une valeur valid!")

        if choice == 1:
            print("Ajouter: ")
            product_name = input("Entrez le produit : ")
            product_quantite = int(input("Entrez la quantite du produit : "))
            product_prix = float(input("Entrez le prix du produit : "))
            ajout_produit(product_name, product_quantite, product_prix)
        elif choice == 2:
            product_name = input("Entrez le produit : ")
            supression_produit(product_name)
        elif choice == 3:
            print("Update: ")
            product_name = input("Entre le nome de produit: ")
            product_quantity = int(input("Entre le quantite du produit: "))
            product_price = int(input("Entre le prix du produit: "))
            update_product(
                product_name,
                new_product_quantity=product_quantity,
                new_product_price=product_price,
            )
        elif choice == 4:
            print("Afficher: ")
            display_products(df, 15)
        elif choice == 5:
            print("stats: ")
            min_price, max_price, avg_price, total_stock = get_stats(df).values()
            print("Min price: ", min_price)
            print("Max price: ", max_price)
            print("Average price: ", avg_price)
            print("Total stock: ", total_stock)

        elif choice == 6:
            print("Afficher Graphique en barres : quantité par produit: ")
            display_pie_chart(df)
        elif choice == 7:
            print("Répartition de la valeur totale du stock par produit: ")
            plot_quantite_par_produit(df)
        elif choice == 8:
            break
        else:
            print("Votre choix n'est pas valide. Merci d'essai une autre fois")
