import pandas as pd

df = pd.read_csv("data/Products.csv")


def update_product(
    product_name: str, new_product_quantity=None, new_product_price=None
):
    if product_name in df["nom_produit"].values:
        if new_product_quantity is not None:
            df.loc[df["nom_produit"] == product_name, "quantite"] = new_product_quantity

        if new_product_price is not None:
            df.loc[df["nom_produit"] == product_name, "prix_unitaire"] = (
                new_product_price
            )

        df.to_csv("data/Products.csv", index=False)
        print(f"Product '{product_name}' successfully added!.")
    else:
        print(f"Product '{product_name}' not found.")


def display_products(df, num_of_lines=5):
    for index, row in df.iterrows():
        if num_of_lines is not None and num_of_lines <= index:
            break
        print(
            f"  - Product {index + 1}: {row['nom_produit']}, Qty: {row['quantite']}, Price: {row['prix_unitaire']}"
        )

    # to display results as a dataframe (table)
    # print(df.head(num_of_lines))


def ajout_produit(product_name, product_quantite, product_prix):
    if product_name in df["nom_produit"].values:
        print("Le produit existe déjà.")
    else:
        try:
            new_product = {
                "nom_produit": product_name,
                "quantite": int(product_quantite),
                "prix_unitaire": float(product_prix),  #
            }
            df.loc[len(df)] = new_product
            df.to_csv("data/Products.csv", index=False)
            print("Produit ajouté avec succès !")
        except ValueError:
            print(
                "Erreur : La quantité doit être un entier et le prix doit être un nombre."
            )


def supression_produit(product_name):
    if product_name in df["nom_produit"].values:
        df.drop(df[df["nom_produit"] == product_name].index, inplace=True)
        df.to_csv("data/Products.csv", index=False)
        print("Produit supprimé avec succès !")
    else:
        print("Le produit n'existe pas.")
