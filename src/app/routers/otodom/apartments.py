from fastapi import APIRouter, Query, Depends, status
from datetime import date
from sqlalchemy.orm import Session

from db.orm import get_session
from db.models.otodom.apartments import OtodomApartments
from app.models.otodom.apartments import OtodomApartmentsResponse
from db.filtering.otodom.apartments import filter_apartments
from db.sorting import sort_results


router = APIRouter()


@router.get("", response_model=OtodomApartmentsResponse, status_code=status.HTTP_200_OK,
            tags=["otodom", "apartments"])
def otodom_apartments(min_price: int = Query(None, alias="minPrice"),
                      max_price: int = Query(None, alias="maxPrice"),
                      min_area: int = Query(None, alias="minArea"),
                      max_area: int = Query(None, alias="maxArea"),
                      min_m2_price: int = Query(None, alias="minM2Price"),
                      max_m2_price: int = Query(None, alias="maxM2Price"),
                      min_build_year: int = Query(None, alias="minBuildYear"),
                      max_build_year: int = Query(None, alias="maxBuildYear"),
                      min_offer_date: date = Query(None, alias="minOfferDate"),
                      max_offer_date: date = Query(None, alias="maxOfferDate"),
                      advertiser: str = Query(None),
                      province: str = Query(None),
                      city: str = Query(None),
                      market: str = Query(None),
                      sort_by: str = Query(None, alias="sortBy"),
                      sort_direction: str = Query(None, alias="sortDirection"),
                      limit: int = Query(20),
                      session: Session = Depends(get_session)):

    query = session.query(OtodomApartments)
    query = filter_apartments(query, min_price, max_price, min_area, max_area, min_m2_price,
                              max_m2_price, min_build_year, max_build_year, min_offer_date,
                              max_offer_date, advertiser, province, city, market)
    query = sort_results(query, sort_by, sort_direction, "otodom", "apartments")
    if limit:
        query = query.limit(limit)

    data = query.all()

    response = OtodomApartmentsResponse(
        is_success=True,
        n_of_results=len(data),
        results=data
    )
    return response
