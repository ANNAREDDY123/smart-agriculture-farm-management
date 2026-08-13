from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.farms import router as farm_router
from routes.fields import router as field_router
from routes.crops import router as crop_router
from routes.irrigation import router as irrigation_router
from routes.treatment import router as treatment_router
from routes.harvest import router as harvest_router
from routes.sale import router as sale_router
from routes.crop_health import router as crop_health_router

app = FastAPI(
    title="Smart Agriculture & Farm Management System"
)


app.include_router(auth_router)
app.include_router(farm_router)
app.include_router(field_router)
app.include_router(crop_router)
app.include_router(irrigation_router)
app.include_router(treatment_router)
app.include_router(harvest_router)
app.include_router(sale_router)
app.include_router(crop_health_router)

@app.get("/")
def root():
    return {
        "message": "Smart Agriculture & Farm Management System is running"
    }
