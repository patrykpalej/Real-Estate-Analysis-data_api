from pydantic import BaseModel
from datetime import datetime


class Land(BaseModel):
    url: str
    title: str
    price: int
    land_area: int
    advertiser_type: str
    utc_created_at: datetime
    province: str
    city: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True


class OtodomLandsResponse(BaseModel):
    is_success: bool
    n_of_results: int
    results: list[Land]
