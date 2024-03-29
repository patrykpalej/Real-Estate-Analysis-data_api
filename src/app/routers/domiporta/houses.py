from fastapi import APIRouter, Query, Depends, status
from sqlalchemy.orm import Session

from db.orm import get_session
from db.models.domiporta.houses import DomiportaHouses
from app.models.domiporta.houses import DomiportaHousesResponse
from db.filtering.domiporta.houses import filter_houses
from db.sorting import sort_results


router = APIRouter()


@router.get("", response_model=DomiportaHousesResponse, status_code=status.HTTP_200_OK,
            tags=["otodom", "houses"])
def otodom_houses(min_price: int = Query(None, alias="minPrice"),
                  max_price: int = Query(None, alias="maxPrice"),
                  min_area: int = Query(None, alias="minArea"),
                  max_area: int = Query(None, alias="maxArea"),
                  min_m2_price: int = Query(None, alias="minM2Price"),
                  max_m2_price: int = Query(None, alias="maxM2Price"),
                  min_build_year: int = Query(None, alias="minBuildYear"),
                  max_build_year: int = Query(None, alias="maxBuildYear"),
                  province: str = Query(None),
                  city: str = Query(None),
                  sort_by: str = Query(None, alias="sortBy"),
                  sort_direction: str = Query(None, alias="sortDirection"),
                  limit: int = Query(20),
                  session: Session = Depends(get_session)):

    query = session.query(DomiportaHouses)
    query = filter_houses(query, min_price, max_price, min_area, max_area, min_m2_price,
                          max_m2_price, min_build_year, max_build_year, province, city)
    query = sort_results(query, sort_by, sort_direction, "domiporta", "houses")
    if limit:
        query = query.limit(limit)

    data = query.all()

    response = DomiportaHousesResponse(
        is_success=True,
        n_of_results=len(data),
        results=data
    )
    return response
