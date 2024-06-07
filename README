# AutoDubber

AutoDubber is an AI-driven application that automatically dubs videos into different languages. It extracts audio from a video file, transcribes the audio using Google Speech-to-Text API, translates the transcription using Google Translate API, converts the translated text into speech using Google Text-to-Speech API, and synchronizes the new audio with the original video.

## Features

- Extracts audio from video files
- Transcribes audio using Google Speech-to-Text API
- Translates transcription to the target language using Google Translate API
- Converts translated text to speech using Google Text-to-Speech API
- Synchronizes the new audio with the original video

## Requirements

- Python 3.8 or higher
- Google Cloud Service Account Key
- FFmpeg

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/AutoDubber.git
    cd AutoDubber
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install FFmpeg:**

    Download and install FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html) and ensure it's added to your system PATH.

5. **Set up Google Cloud Service Account:**

    - Go to [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing project.
    - Enable the following APIs:
        - Google Cloud Speech-to-Text API
        - Google Cloud Text-to-Speech API
        - Google Cloud Translation API
    - Create a service account and download the JSON key file.
    - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the JSON key file.

    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"  # macOS/Linux
    set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\service-account-file.json"  # Windows
    ```

## Usage

1. **Run the auto-dubbing script:**

    ```sh
    python main.py
    ```

2. **Example usage in code:**

    ```python
    import os
    from google.cloud import speech

    def transcribe_audio(audio_path):
        client = speech.SpeechClient()

        with io.open(audio_path, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        try:
            response = client.recognize(config=config, audio=audio)
            for result in response.results:
                print("Transcript: {}".format(result.alternatives[0].transcript))
        except Exception as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    # Set the path to your audio file
    audio_path = "output_audio.wav"
    transcribe_audio(audio_path)
    ```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Google Cloud](https://cloud.google.com/) for their powerful APIs.
- [FFmpeg](https://ffmpeg.org/) for their invaluable multimedia framework.
