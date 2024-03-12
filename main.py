import speech_recognition as sr
import os
import asyncio as aio
import pyttsx3


async def speak(x):
    engine = pyttsx3.init()
    engine.say(x)
    return engine.runAndWait()


if __name__ == '__main__':
    print("Kira")
    aio.run(speak("Hello, I'm Jarvis. How may I assist you"))
