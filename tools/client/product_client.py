import requests

class ProductClient:
    def __init__(self, base_url):
        self.BASE_URL = base_url

    def get_product_by_id(self, id):
        response = requests.get(f"{self.BASE_URL}/{id}")
        return response.json()

    def get_all_products(self):
        response = requests.get(self.BASE_URL)
        return response.json()

    def get_all_products_by_newest(self):
        response = requests.get(f"{self.BASE_URL}/newest")
        return response.json()

    def filter_products(self, name=None, category=None, brand=None, min_rating=None):
        params = {
            "name": name,
            "category": category,
            "brand": brand,
            "minRating": min_rating
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        response = requests.get(f"{self.BASE_URL}/filter", params=params)
        return response.json()

    def get_by_category(self, category):
        response = requests.get(f"{self.BASE_URL}/category/{category}")
        return response.json()
