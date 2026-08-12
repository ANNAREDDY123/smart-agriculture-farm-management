from fastapi import FastAPI

app = FastAPI(
    title="Smart Agriculture & Farm Management System"
)


@app.get("/")
def root():
    return {
        "message": "Smart Agriculture & Farm Management System is running"
    }
