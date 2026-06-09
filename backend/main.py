from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(
    title="SixTech Workspace",
    description="Multi-Agent AI Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "platform": "SixTech Workspace",
        "status": "online",
        "version": "1.0.0"
    }

app.include_router(router)