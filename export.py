import pandas as pd
import click
from utils import fetch_products

@click.command()
@click.option('--output', default="products.xlsx", help="Output Excel file name")
def export_products(output):
    """Export product details (ID, Name, Regular Price, Sale Price) to an Excel file."""
    all_products = []
    page = 1

    while True:
        products = fetch_products(page)
        if not products:
            break  # No more products to fetch

        for product in products:
            all_products.append({
                "id": product["id"],
                "name": product.get("name", "Unnamed Product"),
                "regular_price": product.get("regular_price", ""),
                "sale_price": product.get("sale_price", "")
            })
        page += 1

    df = pd.DataFrame(all_products)
    df.to_excel(output, index=False)
    click.echo(f"Exported {len(all_products)} products to {output}")

if __name__ == "__main__":
    export_products()
