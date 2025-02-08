import requests
import logging
from requests.exceptions import RequestException
from config import WC_API_URL, WC_CONSUMER_KEY, WC_CONSUMER_SECRET, HEADERS

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_products(page=1, per_page=100):
    """Fetch products from WooCommerce API."""
    try:
        params = {
            "consumer_key": WC_CONSUMER_KEY,
            "consumer_secret": WC_CONSUMER_SECRET,
            "per_page": per_page,
            "page": page,
        }
        response = requests.get(WC_API_URL, params=params, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logging.error(f"Failed to fetch products: {e}")
        return []

def update_product_prices(products):
    """Update product prices via batch request."""
    try:
        data = {"update": products}
        params = {
            "consumer_key": WC_CONSUMER_KEY,
            "consumer_secret": WC_CONSUMER_SECRET,
        }
        response = requests.put(f"{WC_API_URL}/batch", params=params, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logging.error(f"Failed to update products: {e}")
        return None
