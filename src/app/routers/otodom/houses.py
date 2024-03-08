from fastapi import APIRouter


router = APIRouter()


@router.get("", tags=["otodom", "houses"])
def otodom_houses():
    return {"hello": "houses"}
