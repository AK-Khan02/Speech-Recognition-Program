import speech_recognition as sr
import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define actions for voice commands
def create_note():
    print("Creating a note...")

def set_reminder():
    print("Setting a reminder...")

# Process the recognized text using NLP and perform actions based on commands
def process_commands(text):
    doc = nlp(text)
    # Example: look for "note" or "reminder" in the text and decide the action
    if "note" in text:
        create_note()
    elif "reminder" in text:
        set_reminder()

def recognize_speech_from_source(recognizer, source):
    # Capture audio
    with source as audio_source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(audio_source)
        audio = recognizer.listen(audio_source)

    # Recognize speech
    try:
        response = recognizer.recognize_google(audio)
        print(f"You said: {response}")
        process_commands(response)
    except sr.RequestError:
        print("API unavailable")
    except sr.UnknownValueError:
        print("Unable to recognize speech")

# Main function to run the enhanced speech recognition
def main():
    # Choose the input source: microphone or audio file
    source_type = input("Choose input source (mic/file): ").strip().lower()
    if source_type == "mic":
        microphone = sr.Microphone()
        recognize_speech_from_source(recognizer, microphone)
    elif source_type == "file":
        audio_file = input("Enter the path to the audio file: ").strip()
        audio_source = sr.AudioFile(audio_file)
        recognize_speech_from_source(recognizer, audio_source)
    else:
        print("Invalid input source.")

if __name__ == "__main__":
    main()
