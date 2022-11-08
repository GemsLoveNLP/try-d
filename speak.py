import azure.cognitiveservices.speech as speechsdk
import nltk

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

def num_extract(s):
    num = []
    ope = []
    #rid the " " sign
    s = s[1:-1]
    #destroy the punctuations
    if s[-1] in ".,?":
        s = s[:-1]
    #create the number and operand lists
    for i in s.split():
        if i.isnumeric():
            num.append(i)
        elif i in "+-*/":
            ope.append(i)
    #check if it is executable
    if len(ope) + 1 == len(num):
        #form the source code and evaluate
        eq = [num[i] + " " + ope[i] for i in range(len(ope))]+[num[-1]]
        value = eval(" ".join(eq))
        #output
        ans = f'"{" ".join(eq)} equals {value}"'
        speech_synthesizer.speak_text_async(ans)
        return ans
    return ""

#print(num_extract("Can you do like 2 + 2 + 15?"))

def num_extract2(s):
    tokens = nltk.word_tokenize(s)
    num = []
    ope = []
    for i in tokens:
        if i.isnumeric():
            num.append(i)
        elif i in "+-*/":
            ope.append(i)
    #check if it is executable
    if len(ope) + 1 == len(num):
        #form the source code and evaluate
        eq = [num[i] + " " + ope[i] for i in range(len(ope))]+[num[-1]]
        value = eval(" ".join(eq))
        #output
        ans = f'"{" ".join(eq)} equals {value}"'
        speech_synthesizer.speak_text_async(ans)
        return ans
    return tokens

print(num_extract2("'Can you do like 2 + 2 + 15?'"))
