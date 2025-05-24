from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import yt_dlp
import os
import uuid

app = FastAPI()

TEMP_DIR = "downloads"
os.makedirs(TEMP_DIR, exist_ok=True)


@app.get("/mp3")
def descargar_mp3(url: str = Query(..., description="URL del video de YouTube")):
    video_id = str(uuid.uuid4())
    output_template = os.path.join(TEMP_DIR, f"{video_id}.%(ext)s")

    opciones = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "quiet": True,
        "noplaylist": True,
        "cookiefile": "cookies.txt",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=True)
            mp3_filename = f"{video_id}.mp3"
            mp3_path = os.path.join(TEMP_DIR, mp3_filename)

            if not os.path.exists(mp3_path):
                raise HTTPException(
                    status_code=404, detail="No se generó el archivo MP3."
                )

            # 🔁 Aquí devolvemos un JSON con el link
            return JSONResponse(
                content={
                    "title": info["title"],
                    "download_url": f"/downloads/{mp3_filename}",
                }
            )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Servir archivos estáticos en /downloads
from fastapi.staticfiles import StaticFiles

app.mount("/downloads", StaticFiles(directory=TEMP_DIR), name="downloads")
