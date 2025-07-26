from fastapi import FastAPI, APIRouter

from api import router

app = FastAPI(
    title="Empty",
    description="Empty",
    version="0.0.1",
    contact={
        "name": "Ivan Levchuk",
        "email": "swankyyy1@gmail.com",
    },
    docs_url="/",
    redoc_url=None,
)


# Init healthcheck
@app.get("/health")
async def health():
    return {"status": "okay"}

app.include_router(router)
