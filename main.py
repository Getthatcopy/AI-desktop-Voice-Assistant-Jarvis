import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiProcess(command):
    import openai
    
    # Replace 'YOUR_API_KEY' with your actual OpenAI API key
    api_key = "API"
    client = openai.Client(api_key=api_key)
    
    # Example chat completion request
    completion = client.chat_completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like answering questions, performing calculations, and managing tasks."},
            {"role": "user", "content": command}
        ]
    )
    
    return completion

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open twitter" in command.lower():
        webbrowser.open("https://www.twitter.com/")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link =musicLibrary.music[song]
        webbrowser.open(link)
    elif 
    else:
        output=aiProcess(command)
        speak(output)
       

if __name__ == "__main__":
    speak("Initializing JARVIS")
    while True:
        # Obtain audio from the microphone
        with sr.Microphone() as source:
            print("Listening...")
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)
                print("Recognizing...")
                try:
                    command = recognizer.recognize_google(audio).lower()
                    print("You said:", command)
                    if "jarvis" in command:
                        speak("Yes, how can I help you?")
                        print("Jarvis Active...")
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
