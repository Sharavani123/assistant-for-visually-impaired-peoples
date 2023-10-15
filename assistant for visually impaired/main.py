import functions
import yolopy
import speech
import cv2
import os
import detect
import datetime

# Set the path to your 'api-key.json' file
api_key_filename = "api-key.json"


# Create a function to load the service account info
def load_service_account_info(filename):
    try:
        with open(filename, "r") as json_file:
            service_account_info = json.load(json_file)
        return service_account_info
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Load the service account info from 'api-key.json'
service_account_info = load_service_account_info(api_key_filename)

# Check if service_account_info is not None before initializing the engine
if service_account_info is not None:
    engine = speech.speech_to_text(service_account_info)
else:
    print("Error: Service account info not loaded.")

labelsPath = "coco.names"  # Correct this path to the "coco.names" file

weightsPath = "yolo/yolov3.weights"
configPath = "yolo/yolov3.cfg"
args = {"threshold": 0.3, "confidence": 0.5}
project_id = "blindbot-4f356"

# Create a function to load the service account info
def load_service_account_info(filename):
    try:
        with open(filename, "r") as json_file:
            service_account_info = json.load(json_file)
        return service_account_info
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None  # You can choose to return None or raise an exception here.

# Specify the path to your 'api-key.json' file
api_key_filename = "/path/to/api-key.json" # Replace with the actual path

# Load the service account info from 'api-key.json'
service_account_info = load_service_account_info(api_key_filename)
# Check if service_account_info is not None before initializing the engine
if service_account_info is not None:
    engine = speech.speech_to_text(service_account_info)
else:
    print("Error: Service account info not loaded.")

# Initialize the speech-to-text engine
# Initialize the speech-to-text engine
engine = speech.speech_to_text(service_account_info)


model = yolopy.yolo(labelsPath, weightsPath, configPath)
listening = False
intent = None
while True:
    cam = cv2.VideoCapture(1)
    if not listening:
        resp = engine.recognize_speech_from_mic()
        print(resp)
        if resp is not None:
            intent, text = detect.detect_intent_texts(project_id, 0, [resp], 'en')
        if intent == 'Jyoti' and resp is not None:
            listening = True
    else:
        engine.text_speech("What can I help you with?")
        intent = ''
        engine.text_speech("Listening")
        resp = engine.recognize_speech_from_mic()
        engine.text_speech("Processing")
        if resp is not None:
            print(resp)
            intent, text = detect.detect_intent_texts(project_id, 0, [resp], 'en')
        if intent == 'Describe':
            detect.describeScene(cam, model, engine)
        elif intent == 'endconvo':
            print(text)
            listening = False
            engine.text_speech(text)
        elif intent == 'Brightness':
            engine.text_speech("It is {} outside".format((functions.getBrightness(cam))[0]))
        elif intent == "FillForm":
            detect.detect_form(cam, engine)
        elif intent == "Read":
            print("read")
            detect.detect_text(cam, engine)
        elif intent == "Time":
            currentDT = datetime.datetime.now()
            engine.text_speech("The time is {} hours and {} minutes".format(currentDT.hour, currentDT.minute))
        elif resp != 'None':
            engine.text_speech(text)
    cam.release()
