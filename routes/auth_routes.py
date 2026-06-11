from fastapi import APIRouter
from fastapi.responses import HTMLResponse

auth_router = APIRouter(prefix="/auth", tags=["auth"]);

@auth_router.get("/")
async def auth():
    return {"message": "Login bem-sucedido"}