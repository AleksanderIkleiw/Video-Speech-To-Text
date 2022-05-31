import speech_recognition as sr

def get_text(file, num_of_operation, queue):
    r = sr.Recognizer()
    audiofile = sr.AudioFile(file)
    with audiofile as source:
        audio = r.record(source)
    queue.put([r.recognize_google(audio, language="pl-PL"), num_of_operation])


