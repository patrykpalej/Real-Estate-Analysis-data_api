from fastapi import APIRouter


router = APIRouter()


@router.get("", tags=["otodom", "lands"])
def otodom_lands():
    return {"hello": "lands"}
