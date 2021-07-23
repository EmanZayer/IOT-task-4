import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using IBM Speech to Text
# Insert API Key in place of 
# 'YOUR UNIQUE API KEY'
IBM_USERNAME = "apikey"  
IBM_PASSWORD = "YOUR UNIQUE API KEY"
result= r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)

try:
       print("IBM Speech to Text thinks you said " + result)
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))

    # save STT as txt file
with open('my_result.txt',mode ='w') as file: 
   file.write("Recognized text:") 
   file.write("\n") 
   file.write(result) 
print("Exporting process completed!")