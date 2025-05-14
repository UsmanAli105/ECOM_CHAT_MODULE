from pydantic import BaseModel
from langchain_core.tools import tool
from tools.client.product_client import ProductClient
from tools.constants import *
from tools.util import *
from typing import List


# Models
class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category: str
    stock: int
    brand: str
    rating: float
    imageUrl: str


# Schemas
class GetAllProductsSchema(BaseModel):
    pass

class FormatAllProductsSchema(BaseModel):
    products: List[Product]

class GetProductsByCategory(BaseModel):
    category: str

class GetProductsByFilter(BaseModel):
    name: str
    category: str
    brand: str
    minRating: str


# helper functions
def generate_product_table_row(product: Product) -> str:
    table_row = f"""
    <tr>
        <td>{product.name}</td>
        <td>
            <div id="desc_{product.id}" style="display: none;">
                {product.description}
            </div>
            <button onclick="toggleDescription('{product.id}')">Read More</button>
        </td>
        <td>{product.price}</td>
        <td>{product.category}</td>
        <td>{product.stock}</td>
        <td>{product.brand}</td>
        <td>{product.rating}</td>
    </tr>
    """
    return table_row


@tool(
    args_schema=FormatAllProductsSchema,
    description="Call this tools when you want to show a product by giving it a list of products.",
)
def generate_product_table(products: list) -> str:
    # Start the HTML table
    table_html = """
    <table border="1" cellpadding="5" cellspacing="0">
        <thead>
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Price</th>
                <th>Category</th>
                <th>Stock</th>
                <th>Brand</th>
                <th>Rating</th>
            </tr>
        </thead>
        <tbody>
    """

    # Add each product row to the table
    for product in products:
        table_html += generate_product_table_row(product)

    # Close the HTML table tags
    table_html += """
        </tbody>
    </table>

    <script>
        function toggleDescription(productId) {
            var descElement = document.getElementById('desc_' + productId);
            var button = descElement.nextElementSibling;

            if (descElement.style.display === 'none') {
                descElement.style.display = 'block';
                button.innerText = 'Read Less';
            } else {
                descElement.style.display = 'none';
                button.innerText = 'Read More';
            }
        }
    </script>
    """

    return table_html



@tool(
    args_schema=GetAllProductsSchema,
    description="Call this api when all the available products are to be shown",
)
def get_all_products():
    try:
        product_data = ProductClient(format_url(BASE_URL, PRODUCTS)).get_all_products()
        products = [Product(**product) for product in product_data]
        return products
    except Exception as e:
        return {"error": "Something went wrong, please try again later."}


@tool(
    args_schema=GetProductsByCategory,
    description="Call this api when products with specific categories are to be shown",
)
def get_product_by_category(category: str):
    try:
        product_data = ProductClient(format_url(BASE_URL, PRODUCTS)).get_by_category(category)
        products = [Product(**product) for product in product_data]
        return products
    except Exception as e:
        return {"error": "Something went wrong, please try again later."}

@tool(
    args_schema=GetProductsByFilter,
    description="Call this api when products with specific filter like name, category, brand, minRating are to be shown. if a filter attribute doesn't exists simply pass empty string for that.",
)
def get_product_by_filter(name: str, category: str, brand: str, minRating: str):
    try:
        product_data = ProductClient(format_url(BASE_URL, PRODUCTS)).filter_products(name, category, brand, minRating)
        products = [Product(**product) for product in product_data]
        return products
    except Exception as e:
        return {"error": "Something went wrong, please try again later."}
