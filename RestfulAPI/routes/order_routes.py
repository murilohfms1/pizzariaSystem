from fastapi import APIRouter
from starlette.responses import FileResponse

order_router = APIRouter()


@order_router.get("/menu", tags=["menu"])
async def menu():
    return FileResponse("pages/menu.html", media_type="text/html")

@order_router.get("/menuStyles.css")
async def menuStyles():
    return FileResponse("styles/menuStyles.css", media_type="text/css")


@order_router.get("/login", tags=["login"])
async def cart():
    return FileResponse("pages/login.html", media_type="text/html")


@order_router.get("/cart", tags=["cart"])
async def cart():
    return FileResponse("pages/cart.html", media_type="text/html")


@order_router.get("/cartStyles.css")
async def cartStyles():
    return FileResponse("styles/cartStyles.css", media_type="text/css")