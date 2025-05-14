from pydantic import BaseModel
from langchain_core.tools import tool
from tools.client.brand_client import BrandClient
from tools.constants import *
from tools.util import *


class Brand(BaseModel):
    id: str
    name: str

class GetAllBrandsSchema(BaseModel):
    pass

@tool(
    args_schema=GetAllBrandsSchema,
    description="Call this tool when you want to get all available brands.",
)
def get_all_brands() -> dict[str, str] | list[Brand]:
    try:
        brand_data = BrandClient(format_url(BASE_URL, BRANDS)).get_all_brands()
        brands = [Brand(**brand) for brand in brand_data]
        return brands
    except Exception as e:
        return {"error": "Something went wrong, please try again later."}
