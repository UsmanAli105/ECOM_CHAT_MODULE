from pydantic import BaseModel
from langchain_core.tools import tool
from tools.client.category_client import CategoryClient
from tools.constants import *
from tools.util import *


class Category(BaseModel):
    id: str
    name: str

class GetAllCategorySchema(BaseModel):
    pass

@tool(
    args_schema=GetAllCategorySchema,
    description="Call this tool when you want to get all available categories.",
)
def get_all_category() -> dict[str, str] | list[Category]:
    try:
        category_data = CategoryClient(format_url(BASE_URL, CATEGORIES)).get_all_categories()
        categories = [Category(**category) for category in category_data]
        return categories
    except Exception as e:
        return {"error": "Something went wrong, please try again later."}
