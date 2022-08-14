#import the necessary library
import speech_recognition as sr


#Class initialisation
r=sr.Recognizer()

#Using the audio_files_harvard file as input 
# sample = sr.AudioFile('audio_files_harvard.wav')
# with sample as source:
#     audio = r.record(source)

#     # If API is unreachable ,exception Handling is used
# try:
#     text = r.recognize_google(audio)
#     print(text)
# except:
#     print("Couldn't read, try again....")



# To use microphone as source
s=sr.Microphone()
with s as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time's up")
    

try:
    text=r.recognize_google(audio_text) 
    print("Text: "+ text)
except:
    print("Sorry, couldn't recognise")










