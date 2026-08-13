from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.farms import router as farm_router

app = FastAPI(
    title="Smart Agriculture & Farm Management System"
)

app.include_router(auth_router)
app.include_router(farm_router)


@app.get("/")
def root():
    return {
        "message": "Smart Agriculture & Farm Management System is running"
    }
