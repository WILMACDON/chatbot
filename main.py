import openai
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.9,
        max_tokens = 150,
    )
    return response.choices[0].text

def main():
    # Configure the speech engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Initialize the speech recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

    while True:
        print("Type 't' for text input, or 's' for speech input:")
        choice = input()

        if choice.lower() == 't':
            print('Enter your question:')
            myQn = input()
            response_text = askGPT(myQn)
            print(response_text)
            engine.say(response_text)
            engine.runAndWait()
        elif choice.lower() == 's':
            print('Say something!')
            with sr.Microphone() as source:
                audio = r.listen(source)

            try:
                myQn = r.recognize_google(audio)
                print(f"You said: {myQn}")
                response_text = askGPT(myQn)
                print(response_text)
                engine.say(response_text)
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                continue
        else:
            print("Invalid choice. Please enter 't' or 's'.")
            continue

main()
