import requests

class CategoryClient:
    def __init__(self, base_url):
        self.BASE_URL = base_url

    def get_category_by_id(self, id):
        response = requests.get(f"{self.BASE_URL}/{id}")
        return response.json()

    def get_all_categories(self):
        response = requests.get(self.BASE_URL)
        return response.json()