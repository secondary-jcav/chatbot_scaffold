from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.post import router as post_router
from routers.get import router as get_router
import uvicorn

app = FastAPI()
app.include_router(post_router)
app.include_router(get_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
