# Advanced Speech Recognition with NLP Command Processing

## Objective

This program aims to provide an advanced interface for speech recognition combined with Natural Language Processing (NLP). It allows users to input voice commands through a microphone or an audio file, which the program then processes to understand and execute specific actions, such as creating notes or setting reminders.

## How It Works

The program operates in several key steps:

1. **Speech Recognition**: Captures speech from the user via a microphone or an audio file and converts it to text using the Google Web Speech API.
2. **Command Processing**: Processes the transcribed text with spaCy, an NLP library, to understand the intent and content of the command.
3. **Action Execution**: Based on the understood command, the program executes predefined actions, such as creating a note or setting a reminder.

## Requirements

- Python 3.x
- SpeechRecognition
- PyAudio (for microphone input)
- spaCy
- en_core_web_sm (spaCy's English language model)

## Installation

First, ensure Python and pip are installed on your system. Then, install the required libraries using pip:

```bash
pip install SpeechRecognition pyaudio spacy
python -m spacy download en_core_web_sm
```

Note: PyAudio installation might require additional steps depending on your system. Refer to the PyAudio documentation for detailed instructions.

## How to Use

1. **Choose Input Source**: Start the program, and when prompted, choose the input source by typing `mic` for microphone input or `file` to specify an audio file path.
   
2. **Speak or Play Audio**: If using a microphone, speak your command after the prompt. If using an audio file, ensure the path is correctly entered when prompted.

3. **Review Output**: The program will transcribe your speech, process the command, and execute the corresponding action, such as creating a note or setting a reminder.

### Example Usage

Run the program:

```bash
python speech_recognition_nlp.py
```

Input source prompt:

```
Choose input source (mic/file): mic
```

After speaking your command, the program processes it and executes the related action.

## Extending the Program

You can extend the program by defining more actions in the `process_commands` function. For example, integrating with APIs to add events to a calendar, send emails, or perform other automated tasks based on voice commands.

---
