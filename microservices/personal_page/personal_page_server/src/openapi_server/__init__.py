from fastapi import FastAPI

from .apis.orders.controllers import personal_page_router


app = FastAPI(
    version="1.0.6",
)

app.include_router(personal_page_router)
