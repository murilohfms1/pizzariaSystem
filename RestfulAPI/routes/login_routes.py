from fastapi import APIRouter
from starlette.responses import FileResponse

login_router = APIRouter();

@login_router.get("/newAccount", tags=["new"])
async def log():
    return FileResponse("pages/new_acc.html", media_type="text/html")