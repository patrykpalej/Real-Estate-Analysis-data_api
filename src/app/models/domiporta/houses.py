from pydantic import BaseModel


class House(BaseModel):
    url: str
    title: str
    price: int
    build_year: int | None
    house_area: float
    province: str
    city: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True


class DomiportaHousesResponse(BaseModel):
    is_success: bool
    n_of_results: int
    results: list[House]
