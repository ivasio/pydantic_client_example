import logging
import sys

from fastapi import FastAPI

from .apis.orders.controllers import personal_page_router


app = FastAPI(
    version="1.0.6",
)

app.include_router(personal_page_router)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

logger = logging.getLogger('fastapi')
logger.setLevel(logging.DEBUG)
