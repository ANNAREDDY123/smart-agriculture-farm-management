from fastapi import FastAPI

from routes.auth import router as auth_router


app = FastAPI(
    title="Smart Agriculture & Farm Management System"
)


app.include_router(
    auth_router
)


@app.get("/")
def root():
    return {
        "message": "Smart Agriculture & Farm Management System is running"
    }
