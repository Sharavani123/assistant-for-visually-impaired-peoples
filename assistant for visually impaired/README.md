
 
Anuj: Assistant for blind
A voice assistant specifically aiming towards aiding the visually imapired.

This system is used to help the visually impaired to have access to the most important features enhancing their living conditions making use of different custom layouts and using speech to text.

More specifically, the system is a chat bot having features solely dedicated towards development of the visually impaired.

Fetaures which make "Anuj" unique:
The system consist of wearable headphones interfaced to Logitech webcam connected to Raspberry PI.

The system performs tasks based on the input (in form of speech) given by the user and responds back as speech.

Key Features:

Description:

Anuj gives a single line description of the surrounding details
Road Conditions: Anuj gives the user an overview of the road conditions, which would further the visually impaired accordingly.
Anuj also specifically mentions if the user is at common places like classrooms, kitchens, bedrooms, etc
Responds the number of people, objects, etc in the frame of the webcam.
Find:

Anuj resonds to commands like find my purse?, check if my watch is in this room? depending upon whether @Entity is present in the frame of the camers
Read:

Anuj also detects text from images and reads it loud.
As a further application it can summarize articles from newspapers.
Fill forms

Anuj also reads out forms (majorly applicable for bank purposes)
Mobile Interactions

It can read out notifications from mobile and as a further application respond to messages, emails, calender, etc
Add ons

Anuj serves the basic features of a chat bot i.e. responds to question including time, lighting conditions, basic wh questions, etc.

Additionally Added frontend GUI 
Tech- stacks used:

1. SpeechRecognizer, Google API for speech to text conversion

2. Python Text to Speech https://pypi.org/project/pyttsx3/

3. Object Recogniiton using *COCO Dataset*

4. Google Cloud Vision API 

5. Dialogflow
Install Dependencies Download the credential for Google Vision API. Copy and paste the files at thr required position.

   git clone https://github.com/mansi1710/DobaraMatPuchana
   cd DobaraMatPuchana
   pip install -r requirements.txt
Run Code:

python main.py
