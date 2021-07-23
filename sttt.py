from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = '9P7jznPleTo06Prh9CEq8me4Svj4GDxx64u1b-JDXbwU'
url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/9ab72ccd-9201-49a9-84d6-cd7fedae1d92'

# Setup Service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# Perform conversion
with open('unt.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

    onfidence = res['results'][0]['alternatives'][0]['confidence']
confidence

with open('output.txt', 'w') as out:
    out.writelines(text)

    # Perform conversion
with open('Untitled.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-AU_NarrowbandModel', continuous=True).get_result()