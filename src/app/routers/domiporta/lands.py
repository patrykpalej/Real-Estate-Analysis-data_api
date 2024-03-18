from fastapi import APIRouter, Query, Depends, status
from sqlalchemy.orm import Session

from db.orm import get_session
from db.models.domiporta.lands import DomiportaLands
from app.models.domiporta.lands import DomiportaLandsResponse
from app.filtering.domiporta.lands import filter_lands


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
                 session: Session = Depends(get_session)):

    query = session.query(DomiportaLands)
    query = filter_lands(query, min_price, max_price, min_area, max_area, min_m2_price,
                         max_m2_price, province, city)

    data = query.all()

    response = DomiportaLandsResponse(
        is_success=True,
        n_of_results=len(data),
        results=data
    )
    return response
