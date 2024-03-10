from pydantic import BaseModel
from datetime import datetime


class House(BaseModel):
    url: str
    title: str
    price: int
    build_year: int | None
    house_area: int
    lot_area: int
    advertiser_type: str
    market: str
    utc_created_at: datetime
    province: str
    city: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True


class OtodomHousesResponse(BaseModel):
    is_success: bool
    n_of_results: int
    results: list[House]
