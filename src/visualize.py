import matplotlib.pylab as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Products.csv")


def display_pie_chart(df):
    quantity = np.array(df["quantite"])
    price_unit = np.array(df["prix_unitaire"])

    product_value = quantity * price_unit
    products_labels = np.array(df["nom_produit"])

    plt.pie(product_value, labels=products_labels)
    plt.show()
