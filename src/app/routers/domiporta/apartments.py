from fastapi import APIRouter


router = APIRouter()


@router.get("", tags=["domiporta", "apartments"])
def domiporta_apartments():
    return {"domiporta": "apartments"}
