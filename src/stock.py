import pandas as pd

df = pd.read_csv('Products.csv')

def ajout_produit(product_name, product_quantite, product_prix):
    if product_name in df['nom_produit'].values:
        print("Le produit existe déjà.")
    else:
        try:
            new_product = {
                'nom_produit': product_name,
                'quantite': int(product_quantite),
                'prix_unitaire': float(product_prix)  #
            }
            df.loc[len(df)] = new_product
            df.to_csv('Products.csv', index=False)
            print("Produit ajouté avec succès !")
        except ValueError:
            print("Erreur : La quantité doit être un entier et le prix doit être un nombre.")

# def supression_produit(product_name):
#     if product_name in df['nom_produit'].values:
#         df.drop(df[df['nom_produit'] == product_name], inplace=True)
#         df.to_csv('Products.csv', index=False)
#         print("Produit supprimé avec succès !")
#     else :
#         print("Le produit n'existe pas.")

# ajout_produit('Laptop', 10, 800.)
# supression_produit('mouse')


# print(df)
print(df)