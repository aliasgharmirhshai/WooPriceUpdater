# WooCommerce Product Management CLI

## Overview
This command-line tool allows you to manage WooCommerce products efficiently by exporting product data to an Excel file and updating product prices from an Excel file.

## Features
- Export WooCommerce products (ID, Regular Price, Sale Price) to an Excel file.
- Update WooCommerce product prices from an Excel file.
- Secure API authentication using environment variables.
- Error handling and logging for debugging.

## Prerequisites
- Python 3.7+
- WooCommerce store with API access
- WooCommerce REST API credentials (Consumer Key & Secret)

## Installation
Clone the repository and install dependencies:
```sh
 git clone https://github.com/aliasgharmirhshai/WooPriceUpdater.git
 cd woocommerce-cli
 pip install -r requirements.txt
```

### Setup API Credentials
1. Create a `.env` file in the project root.
2. Add your WooCommerce API credentials:
```sh
SITE=https://<your-site>/wp-json/wc/v3/products
WC_CONSUMER_KEY=your_key_here
WC_CONSUMER_SECRET=your_secret_here
```

## Usage

### Export Products
Exports WooCommerce products to an Excel file.
```sh
python main.py export-products --output products.xlsx
```

### Update Product Prices
Updates product prices from an Excel file.
```sh
python main.py update-prices products.xlsx
```

## File Structure
```
woocommerce_cli/
│── config.py             # Configuration and API credentials
│── main.py               # CLI entry point
│── export.py             # Product export functionality
│── update.py             # Product update functionality
│── utils.py              # Helper functions
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── .env                  # API credentials (ignored in Git)
```

## Error Handling
- Logs errors and exceptions for debugging.
- Skips invalid rows in Excel files to prevent failures.

## Future Enhancements
- Add support for more WooCommerce product fields.
- Implement batch processing for large data sets.
- Dockerize for deployment.

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push the branch and create a Pull Request.

## Support
For issues, open a GitHub issue or contact me.

