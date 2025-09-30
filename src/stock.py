import pandas as pd

df = pd.read_csv("Products.csv")


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

        df.to_csv("Products.csv", index=False)
        print(f"Product '{product_name}' successfully added!.")
    else:
        print(f"Product '{product_name}' not found.")


def display_products(df, num_of_lines=5):
    for index, row in df.iterrows():
        if num_of_lines is not None and num_of_lines <= index:
            break
        print(
            f"Product {index + 1}: {row['nom_produit']}, Qty: {row['quantite']}, Price: {row['prix_unitaire']}"
        )

    # to display results as a dataframe (table)
    # print(df.head(num_of_lines))
