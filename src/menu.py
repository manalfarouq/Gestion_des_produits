from stock import update_product, display_products
from stats import get_stats
from visualization import display_pie_chart
import pandas as pd

df = pd.read_csv("Products.csv")

choices = [
    "1- Ajouter un produit.",
    "2- Supprimer un produit",
    "3- Modifier la quantité d’un produit",
    "4- Afficher le stock",
    "5- Afficher les statistiques",
    "6- Afficher un graphique ",
    "7- Quitter",
]


def menu():
    while True:
        for choice in choices:
            print(choice)

        try:
            choice = int(input("Entre votre choix: ").strip())
        except ValueError:
            print("Merci d'entre une valeur valid!")

        if choice == 1:
            print("test", choices[0])
        elif choice == 2:
            print(choices[1])
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
            display_products(df, 10)
        elif choice == 5:
            print("stats: ")
            min_price, max_price, avg_price, total_stock = get_stats(df).values()
            print(min_price, max_price, avg_price, total_stock)
        elif choice == 6:
            print("Graphique: ")
            display_pie_chart(df)
        elif choice == 7:
            break
        else:
            print("Votre choix n'est pas valide. Merci d'essai une autre fois")


menu()
