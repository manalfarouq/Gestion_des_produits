import pandas as pd

df = pd.read_csv("data/Products.csv")


def get_min_price(df):
    return df["prix_unitaire"].min()


def get_max_price(df):
    return df["prix_unitaire"].max()


def get_avg_price(df):
    return df["prix_unitaire"].mean()


def sum_multi_price_by_quantity(df):
    results = df["prix_unitaire"] * df["quantite"]
    return results.sum()


def get_stats(df):
    min_price = get_min_price(df)
    max_price = get_max_price(df)
    avg_price = get_avg_price(df)
    total_stock = sum_multi_price_by_quantity(df)

    return {
        "min_price": min_price,
        "max_price": max_price,
        "avg_price": avg_price,
        "total_stock": total_stock,
    }
