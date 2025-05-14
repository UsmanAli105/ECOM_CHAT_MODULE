import requests

class BrandClient:
    def __init__(self, base_url):
        self.BASE_URL = base_url

    def get_all_brands(self):
        response = requests.get(self.BASE_URL)
        return response.json()