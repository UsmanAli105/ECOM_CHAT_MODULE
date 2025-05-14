from typing import List, Optional
from pydantic import BaseModel
from langchain_core.tools import tool
import requests

# ---------- Pydantic Models ----------

class GetDropdownRequest(BaseModel):
    channel: int
    deviceId: str
    deviceType: str

class Category(BaseModel):
    id: int
    name: str

class CategoryData(BaseModel):
    success: bool
    categories: List[Category]

class Status(BaseModel):
    code: int
    message: str

class GetCategoryDropdownResponse(BaseModel):
    status: Status
    data: CategoryData


# ---------- Tool Function ----------

@tool
def fetch_category_dropdown(request_data: GetDropdownRequest) -> Optional[GetCategoryDropdownResponse]:
    """Use this tool to get all the available category ids"""
    url = "http://localhost:8025/api/category/getDropDown"
    headers = {
        "accept": "*/*",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=request_data.model_dump(), headers=headers)
        response.raise_for_status()
        return GetCategoryDropdownResponse.model_validate(response.json())
    except Exception as e:
        print("Error:", e)
        return None


# ---------- Example Usage ----------

if __name__ == "__main__":
    req = GetDropdownRequest(channel=1, deviceId="abcd1234xyz", deviceType="ANDROID")
    res = fetch_category_dropdown(req)

    if res:
        print("Status:", res.status.message)
        for category in res.data.categories:
            print(f"- {category.id}: {category.name}")
