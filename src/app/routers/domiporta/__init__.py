from fastapi import APIRouter

from .apartments import router as apartments_router
from .houses import router as houses_router
from .lands import router as lands_router


router = APIRouter(prefix="/domiporta")
router.include_router(apartments_router, prefix="/apartments")
router.include_router(houses_router, prefix="/houses")
router.include_router(lands_router, prefix="/lands")

