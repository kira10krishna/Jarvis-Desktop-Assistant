import pyttsx3
import speech_recognition as sr
import nltk

class Jarvis:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = self.r.listen(source)
                text = self.r.recognize_google(audio)
                print("You said: " + text)
                return text
            except:
                print("Sorry, I did not get that")
                return self.listen()

    def process_command(self, command):
        # Add your code here to process the user command
        # For example, you can use if-else statements to check for specific commands
        if "hello" in command:
            self.speak("Hello, how can I help you?")
        elif "goodbye" in command:
            self.speak("Goodbye, have a nice day!")
        else:
            self.speak("I'm sorry, I don't understand that command")


# Main loop
if __name__ == "__main__":
    jarvis = Jarvis()
    while True:
        try:
            command = jarvis.listen()
            jarvis.process_command(command)
        except KeyboardInterrupt:
            print("Exiting...")
            break




import speech_recognition as sr

# Set up the recognizer
r = sr.Recognizer()

# Set up the Google Cloud Speech-to-Text API client
# (Replace YOUR_GOOGLE_CLOUD_SPEECH_TO_TEXT_API_KEY with your actual API key)
google_cloud_speech_to_text = sr.Microphone(device_index=0, sample_rate=16000,
                                            chunk_size=2048,
                                            input_mode='audio_file_chunk')

def recognize_google_cloud(audio_data):
    with google_cloud_speech_to_text as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=5)
        text = r.recognize_google_cloud(audio_data, key='YOUR_GOOGLE_CLOUD_SPEECH_TO_TEXT_API_KEY')
        return text