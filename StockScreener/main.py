from typing import Union
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

server = FastAPI()
templates = Jinja2Templates(directory = "templates")


@server.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {
            "request": request
    })


@server.post("/stock")
def create_stock():
    return {
        "code": "Success",
        "message": "Stock created."
    }







