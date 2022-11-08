import azure.cognitiveservices.speech as speechsdk
from speak import *


Speech_key = "3b66785c9d73403b99708544933c45a2"
Region = "southeastasia"
Endpoint = "https://southeastasia.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

speech_config = speechsdk.SpeechConfig(subscription=Speech_key, region = Region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

start()

while True:
    result = speech_recognizer.recognize_once()
    
    f_result = f(result)
    if type(f_result) == str:
        print(f_result)
        if "quit" in f_result.lower():
            print("QUIT")
            break
