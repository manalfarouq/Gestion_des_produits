import pandas as pd

df = pd.read_csv("Products.csv")

print(df)


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

        df.to_csv("Product.csv", index=False)
        print(f"Product '{product_name}' successfully added!.")
    else:
        print(f"Product '{product_name}' not found.")


update_product(product_name="Laptop", new_product_quantity=60)
update_product(product_name="Phone", new_product_price=299.99)

print(df)
