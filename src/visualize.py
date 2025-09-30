import matplotlib.pylab as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/Products.csv")


def display_pie_chart(df):
    quantity = np.array(df["quantite"])
    price_unit = np.array(df["prix_unitaire"])

    product_value = quantity * price_unit
    products_labels = np.array(df["nom_produit"])

    plt.pie(product_value, labels=products_labels)
    plt.show()


def plot_quantite_par_produit(dataframe):
    plt.figure(figsize=(8, 5))
    plt.bar(dataframe["nom_produit"], dataframe["quantite"], color="yellow")
    plt.xlabel("Produits")
    plt.ylabel("Quantité")
    plt.title("Quantité par produit")
    plt.show()
