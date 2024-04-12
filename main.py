import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def main():
    greet()
    speak("How can I assist you today?")
    
    while True:
        command = listen()
        
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {current_date}.")
        elif "youtube" in command:
            webbrowser.open("https://www.youtube.com/?app")
        elif "thank you" in command:
            speak("You're welcome!")
        elif "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
