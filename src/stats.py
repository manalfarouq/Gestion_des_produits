#  stats file

import pandas as pd

df = pd.read_csv('Products.csv')

def afficher_statistiques(dataframe_name):
    total_produits = len(dataframe_name)
    produit_plus_cher = dataframe_name.loc[df['prix_unitaire'].idxmax()]
    produit_moins_cher = dataframe_name.loc[df['prix_unitaire'].idxmin()]

    print(f"Nombre total de produits : {total_produits}")
    print(f"Produit le plus cher : {produit_plus_cher['nom_produit']} à {produit_plus_cher['prix_unitaire']} DH")
    print(f"Produit le moins cher : {produit_moins_cher['nom_produit']} à {produit_moins_cher['prix_unitaire']} DH")
    
