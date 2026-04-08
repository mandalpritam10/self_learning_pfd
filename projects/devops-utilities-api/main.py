from app.api import app
import uvicorn

if __name__ == "__main__":
    #ASGI Web Server
    uvicorn.run(
        "app.api:app", #app location
        host="0.0.0.0",
        port=8000,
        reload=True
    )