import speech_recognition as sr
import asyncio as aio
import pyttsx3
import logging
import os


def setup_logging():
    file_path = "logfile.log"
    logging.basicConfig(
        filename=file_path,
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


setup_logging()


async def speak(text):
    """Asynchronously speaks the given text using pyttsx3.

    Args:
        text (str): The text to be spoken
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    source = sr.Microphone()  # Create an instance of Microphone
    with source as audio_source:  # Use the instance in the with statement
        r.pause_threshold = 1
        audio = r.listen(audio_source)
        print("test0")
        try:

            query = r.recognize_google_cloud(audio, language="en-in")
            print("Test1")
            print(f"User said: {query}")
            logging.info(f"User said: {query}")
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
            logging.error("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from speech recognition service; {e}")
            logging.error(f"Could not request results from speech recognition service; {e}")
    return query  # Return the recognized query


async def main():
    print("Kira")
    await speak("Hello, I am Jarvis, how may I assist you")
    print("Listening....")
    text1 = takeCommand()
    await speak(text1)

if __name__ == '__main__':
    aio.run(main())
