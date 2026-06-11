from fastapi import APIRouter
from starlette.responses import FileResponse

main_router = APIRouter();

@main_router.get("/")
async def home():
    return FileResponse("pages/index.html", media_type="text/html")

@main_router.get("/styles.css")
async def styles():
    return FileResponse("styles/styles.css", media_type="text/css")