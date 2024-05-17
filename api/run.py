# -*- coding: utf-8 -*-
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.config import Settings, get_settings
from api.routes import basic


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("They are executed before lifting the api")
    yield


app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"displayRequestDuration": True})
settings: Settings = get_settings()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(basic.router, prefix="/api", tags=["Basic"])


@app.get("/ping")
async def ping():
    return "pong"
