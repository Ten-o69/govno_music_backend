from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from .routers import api_router
from common.constants import DIR_STATIC

app = FastAPI(
    description="Плейер для говна",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно указать конкретные домены, например: ["https://your-ngrok-url.ngrok.io"]
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, PUT и т.д.)
    allow_headers=["*"],  # Разрешаем все заголовки
)

app.mount("/static", StaticFiles(directory=DIR_STATIC), name="static")


@app.get("/")
def root():
    return {
        "message": "API work!",
    }

app.include_router(api_router)
