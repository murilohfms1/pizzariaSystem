from fastapi import FastAPI

app = FastAPI();

from routes.order_routes import order_router
from routes.auth_routes import auth_router
from routes.main_routes import main_router
from routes.login_routes import login_router

app.include_router(order_router);
app.include_router(auth_router);
app.include_router(main_router);
app.include_router(login_router);


