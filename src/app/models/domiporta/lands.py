from pydantic import BaseModel


class Land(BaseModel):
    url: str
    title: str
    price: int
    land_area: int
    province: str
    city: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True


class DomiportaLandsResponse(BaseModel):
    is_success: bool
    n_of_results: int
    results: list[Land]
