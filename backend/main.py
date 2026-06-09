from fastapi import FastAPI

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