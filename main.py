import click
from export import export_products
from update import update_prices

@click.group()
def cli():
    """WooCommerce Product Management CLI"""
    pass

cli.add_command(export_products)
cli.add_command(update_prices)

if __name__ == '__main__':
    cli()
