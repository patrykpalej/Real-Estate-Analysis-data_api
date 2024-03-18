from pydantic import BaseModel


class Apartment(BaseModel):
    url: str
    title: str
    price: int
    build_year: int | None
    apartment_area: float
    province: str
    city: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True


class DomiportaApartmentsResponse(BaseModel):
    is_success: bool
    n_of_results: int
    results: list[Apartment]
