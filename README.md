# YouTube MP3 & Captions API

This FastAPI application allows you to:
- Download the audio of a YouTube video as an MP3 file.
- (If you add the endpoint) Transcribe YouTube video captions (subtitles) to text from a provided URL.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd transcript-video
   ```

2. Install the required dependencies using [uv](https://astral.sh/uv/):
   ```
   uv pip install fastapi yt-dlp uvicorn youtube-transcript-api pytube
   ```

## Usage

1. Start the FastAPI application:
   ```
   uvicorn main:app --reload
   ```

2. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Endpoints

#### Download MP3

- **GET** `/mp3?url=https://www.youtube.com/watch?v=VIDEO_ID`

  Returns a JSON with the video title and a download link for the MP3 file.

  **Example response:**
  ```json
  {
    "title": "Video Title",
    "download_url": "/downloads/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.mp3"
  }
  ```

- Download the MP3 file from the provided `download_url`.

#### (Optional) Get Captions

If you add a `/captions` endpoint, you can use:

- **GET** `/captions?url=https://www.youtube.com/watch?v=VIDEO_ID`

  Returns a JSON with the transcribed captions.

  **Example response:**
  ```json
  {
    "captions": "Transcribed text from the video's subtitles..."
  }
  ```

## Notes

- The MP3 files are stored in the `downloads` directory and served at `/downloads`.
- Make sure you have `ffmpeg` installed on your system for audio extraction.

## License

This project is licensed under the MIT License.