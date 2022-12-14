import azure.cognitiveservices.speech as speechsdk

Speech_key = "3b66785c9d73403b99708544933c45a2"
Region = "southeastasia"
Endpoint = "https://southeastasia.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

speech_config = speechsdk.SpeechConfig(subscription=Speech_key, region =Region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

def start():
    print("The hearing starts NOW!!!")

def f(result):
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        text_string = (f'"{result.text}"')
        speech_synthesizer.speak_text_async(result.text)
        return text_string