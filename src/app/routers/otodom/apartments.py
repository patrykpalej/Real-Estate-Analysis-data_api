from fastapi import APIRouter


router = APIRouter()


@router.get("", tags=["otodom", "apartments"])
def otodom_apartments():
    return {"hello": "apartments"}
