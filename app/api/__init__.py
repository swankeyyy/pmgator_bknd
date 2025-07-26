from fastapi import APIRouter

from src.settings import settings   

# Init router
router = APIRouter(prefix=settings.API_PREFIX)