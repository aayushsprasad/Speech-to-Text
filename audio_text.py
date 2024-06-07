import speech_recognition as sr

r = sr.Recognizer()

# Replace 'output1.wav' with the path to your WAV file
input_wav_file = 'output1.wav'

try:
    with sr.AudioFile(input_wav_file) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        print("Recognized text:", text)
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except Exception as e:
    print("An error occurred:", e)
