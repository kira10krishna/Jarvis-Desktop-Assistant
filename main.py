# import speech_recognition as sr
# import os
import asyncio as aio
import pyttsx3

async def speak(text):
    """Asynchronously speaks the given text using pyttsx3.

    Args:
        text (str): The text to be spoken
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

async def main():
    await speak("Hello, I am Jarvis, how may I assist youu")
    print("Kira")

if __name__ == '__main__':
    aio.run(main())

