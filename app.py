"""
Запуск:
uvicorn app:app --reload

После открываем в браузере:
http://localhost:8000/video
"""

from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Hallee-Hallo",
    description="Заглушка приложения для проекта по DL"
)

VIDEO_URL = "https://rutube.ru/video/c6cc4d620b1d4338901770a44b3e82f4/"

@app.get("/video", summary="MP4 Redirect")
@app.head("/video", summary="MP4 Redirect (HEAD)")

def redirect_to_video():
    return RedirectResponse(
        url=VIDEO_URL,
        status_code=status.HTTP_302_FOUND,
    )
