def get_min_price(df):
    return df["prix_unitaire"].min()


def get_max_price(df):
    return df["prix_unitaire"].max()


def get_avg_price(df):
    return df["prix_unitaire"].mean()


def get_total_stock(df):
    return df["quantite"].sum()


def get_stats(df):
    min_price = get_min_price(df)
    max_price = get_max_price(df)
    avg_price = get_avg_price(df)
    total_stock = get_total_stock(df)

    return {
        "min_price": min_price,
        "max_price": max_price,
        "avg_price": avg_price,
        "total_stock": total_stock,
    }
