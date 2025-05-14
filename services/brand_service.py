from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_core.tools import tool
import requests

# ---------- Pydantic Models ----------

class GetDropdownRequest(BaseModel):
    channel: int
    deviceId: str
    deviceType: str

class Brand(BaseModel):
    id: int
    name: str

class BrandData(BaseModel):
    success: bool
    brands: List[Brand]

class Status(BaseModel):
    code: int
    message: str

class GetDropdownResponse(BaseModel):
    status: Status
    data: BrandData


# ---------- Tool Function ----------

@tool
def fetch_brand_dropdown(request_data: GetDropdownRequest) -> Optional[GetDropdownResponse]:
    """Use this tool to get all the available brand ids"""
    url = "http://localhost:8025/api/brand/getDropdown"
    headers = {
        "accept": "*/*",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=request_data.model_dump(), headers=headers)
        response.raise_for_status()
        return GetDropdownResponse.model_validate(response.json())
    except Exception as e:
        print("Error:", e)
        return None


# ---------- Example Usage ----------

if __name__ == "__main__":
    req = GetDropdownRequest(channel=1, deviceId="abcd1234xyz", deviceType="ANDROID")
    res = fetch_brand_dropdown(req)

    if res:
        print("Status:", res.status.message)
        for brand in res.data.brands:  # Just print the first 5 for brevity
            print(f"- {brand.id}: {brand.name}")
