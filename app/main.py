from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.farms import router as farm_router
from routes.fields import router as field_router
from routes.crops import router as crop_router
from routes.irrigation import router as irrigation_router


app = FastAPI(
    title="Smart Agriculture & Farm Management System"
)


app.include_router(auth_router)
app.include_router(farm_router)
app.include_router(field_router)
app.include_router(crop_router)
app.include_router(irrigation_router)


@app.get("/")
def root():
    return {
        "message": "Smart Agriculture & Farm Management System is running"
    }
