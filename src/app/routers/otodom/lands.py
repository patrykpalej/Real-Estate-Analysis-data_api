from fastapi import APIRouter, Query, Depends, status
from datetime import date
from sqlalchemy.orm import Session

from db.orm import get_session
from db.models.otodom.lands import OtodomLands
from app.models.otodom.lands import OtodomLandsResponse
from app.filtering.otodom.lands import filter_lands


router = APIRouter()


@router.get("", response_model=OtodomLandsResponse, status_code=status.HTTP_200_OK,
            tags=["otodom", "lands"])
def otodom_lands(min_price: int = Query(None, alias="minPrice"),
                 max_price: int = Query(None, alias="maxPrice"),
                 min_area: int = Query(None, alias="minArea"),
                 max_area: int = Query(None, alias="maxArea"),
                 min_m2_price: int = Query(None, alias="minM2Price"),
                 max_m2_price: int = Query(None, alias="maxM2Price"),
                 min_offer_date: date = Query(None, alias="minOfferDate"),
                 max_offer_date: date = Query(None, alias="maxOfferDate"),
                 advertiser: str = Query(None),
                 province: str = Query(None),
                 city: str = Query(None),
                 session: Session = Depends(get_session)):

    query = session.query(OtodomLands)
    query = filter_lands(query, min_price, max_price, min_area, max_area, min_m2_price,
                         max_m2_price, min_offer_date, max_offer_date, advertiser, province, city)

    data = query.all()

    response = OtodomLandsResponse(
        is_success=True,
        n_of_results=len(data),
        results=data
    )
    return response
