import speech_recognition as sr
import os
import asyncio
import time
import pyttsx3


async def speak(text):
    """Asynchronously speaks the given text using pyttsx3.

    Args:
        text (str): The text to be spoken.
    """

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


async def main():
    """The main asynchronous function that calls speak."""

    start_time = time.time()  # Record start time before initialization

    print("Kira")
    await speak("Hello")

    end_time = time.time()  # Record end time after runAndWait
    # Calculate and print the execution time
    print(f"Speech completed in: {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    asyncio.run(main())

