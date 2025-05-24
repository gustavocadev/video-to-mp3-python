# YouTube Transcriber

This project is a FastAPI application that transcribes YouTube video captions to text from a provided URL. It allows users to input a YouTube video URL and receive the transcribed text as a response.

## Project Structure

```
youtube-transcriber
├── app
│   ├── main.py                # Entry point of the FastAPI application
│   ├── api
│   │   └── transcribe.py      # API endpoints for transcribing YouTube video captions
│   ├── services
│   │   └── youtube_transcriber.py # Logic for fetching and processing YouTube video captions
│   └── models
│       └── transcribe_request.py  # Data model for the transcription request
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-transcriber
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

3. Use the `/transcribe` endpoint to transcribe YouTube video captions. Provide a JSON body with the following structure:
   ```json
   {
       "url": "https://www.youtube.com/watch?v=VIDEO_ID"
   }
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.