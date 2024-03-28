from fastapi import FastAPI

from app.routers.otodom import router as otodom_router
from app.routers.domiporta import router as domiporta_router
from app.middlewares import log_requests


app = FastAPI(
    title="Real Estate Analysis – data API",
    summary="REST API for real estate data acquisition",
    version="0.1.0"
)

app.include_router(otodom_router)
app.include_router(domiporta_router)

app.middleware("http")(log_requests)
