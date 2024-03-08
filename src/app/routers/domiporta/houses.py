from fastapi import APIRouter


router = APIRouter()


@router.get("", tags=["domiporta", "houses"])
def domiporta_houses():
    return {"domiporta": "houses"}
