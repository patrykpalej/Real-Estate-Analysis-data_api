from fastapi import APIRouter, Query, Depends, status
from sqlalchemy.orm import Session

from db.orm import get_session
from db.models.domiporta.apartments import DomiportaApartments
from app.models.domiporta.apartments import DomiportaApartmentsResponse
from app.filtering.domiporta.apartments import filter_apartments


router = APIRouter()


@router.get("", response_model=DomiportaApartmentsResponse, status_code=status.HTTP_200_OK,
            tags=["otodom", "apartments"])
def otodom_apartments(min_price: int = Query(None, alias="minPrice"),
                      max_price: int = Query(None, alias="maxPrice"),
                      min_area: int = Query(None, alias="minArea"),
                      max_area: int = Query(None, alias="maxArea"),
                      min_m2_price: int = Query(None, alias="minM2Price"),
                      max_m2_price: int = Query(None, alias="maxM2Price"),
                      min_build_year: int = Query(None, alias="minBuildYear"),
                      max_build_year: int = Query(None, alias="maxBuildYear"),
                      province: str = Query(None),
                      city: str = Query(None),
                      session: Session = Depends(get_session)):

    query = session.query(DomiportaApartments)
    query = filter_apartments(query, min_price, max_price, min_area, max_area, min_m2_price,
                              max_m2_price, min_build_year, max_build_year, province, city)

    data = query.all()

    response = DomiportaApartmentsResponse(
        is_success=True,
        n_of_results=len(data),
        results=data
    )
    return response
