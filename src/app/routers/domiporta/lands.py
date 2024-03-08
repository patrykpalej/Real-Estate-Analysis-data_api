from fastapi import APIRouter


router = APIRouter()


@router.get("", tags=["domiporta", "lands"])
def domiporta_lands():
    return {"domiporta": "lands"}
