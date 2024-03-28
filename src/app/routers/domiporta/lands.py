from fastapi import APIRouter, Query, Depends, status
from sqlalchemy.orm import Session

from db.orm import get_session
from db.models.domiporta.lands import DomiportaLands
from app.models.domiporta.lands import DomiportaLandsResponse
from db.filtering.domiporta.lands import filter_lands
from db.sorting import sort_results


router = APIRouter()


@router.get("", response_model=DomiportaLandsResponse, status_code=status.HTTP_200_OK,
            tags=["otodom", "lands"])
def otodom_lands(min_price: int = Query(None, alias="minPrice"),
                 max_price: int = Query(None, alias="maxPrice"),
                 min_area: int = Query(None, alias="minArea"),
                 max_area: int = Query(None, alias="maxArea"),
                 min_m2_price: int = Query(None, alias="minM2Price"),
                 max_m2_price: int = Query(None, alias="maxM2Price"),
                 province: str = Query(None),
                 city: str = Query(None),
                 sort_by: str = Query(None, alias="sortBy"),
                 sort_direction: str = Query(None, alias="sortDirection"),
                 limit: int = Query(20),
                 session: Session = Depends(get_session)):

    query = session.query(DomiportaLands)
    query = filter_lands(query, min_price, max_price, min_area, max_area, min_m2_price,
                         max_m2_price, province, city)
    query = sort_results(query, sort_by, sort_direction, "domiporta", "lands")
    if limit:
        query = query.limit(limit)

    data = query.all()

    response = DomiportaLandsResponse(
        is_success=True,
        n_of_results=len(data),
        results=data
    )
    return response
