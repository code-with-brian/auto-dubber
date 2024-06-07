import os
import subprocess
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

def extract_audio_from_video(video_path):
    audio_path = "extracted_audio.wav"
    command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path}"
    subprocess.call(command, shell=True)
    return audio_path

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        print(f"Error details: {e.reason}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def text_to_speech(text, target_language):
    tts = gTTS(text, lang=target_language)
    tts.save("translated_audio.mp3")
    return "translated_audio.mp3"

def lip_sync(video_path, audio_path):
    synced_video_path = "synced_video.mp4"
    command = f"ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a aac {synced_video_path}"
    subprocess.call(command, shell=True)
    return synced_video_path

def auto_dub(video_path, target_language='es'):
    audio_path = extract_audio_from_video(video_path)
    transcript = transcribe_audio(audio_path)
    if transcript:
        print("Transcription: ", transcript)
        translated_text = translate_text(transcript, target_language)
        print("Translated Text: ", translated_text)
        translated_audio_path = text_to_speech(translated_text, target_language)
        synced_video_path = lip_sync(video_path, translated_audio_path)
        print(f"Dubbed video saved to: {synced_video_path}")


# Example usage
auto_dub('korean-sample.mp4')
