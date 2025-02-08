import pandas as pd
import click
from utils import update_product_prices

@click.command()
@click.argument("file")
def update_prices(file):
    """Update only the price fields from an Excel file"""
    try:
        df = pd.read_excel(file)
    except Exception as e:
        click.echo(f"Error reading Excel file: {e}", err=True)
        return
    
    if not {"id", "regular_price"}.issubset(df.columns):
        click.echo("Error: The Excel file must contain 'id' and 'regular_price' columns.", err=True)
        return
    
    products = []
    for _, row in df.iterrows():
        try:
            product_data = {
                "id": int(row["id"]),
                "regular_price": str(row["regular_price"]),
            }
            if "sale_price" in row and pd.notnull(row["sale_price"]):
                product_data["sale_price"] = str(row["sale_price"])
            products.append(product_data)
        except (ValueError, KeyError) as e:
            click.echo(f"Skipping row due to error: {e}", err=True)

    if not products:
        click.echo("No valid products to update.", err=True)
        return
    
    response = update_product_prices(products)
    if response:
        click.echo(f"Successfully updated {len(products)} products.")

if __name__ == "__main__":
    update_prices()
