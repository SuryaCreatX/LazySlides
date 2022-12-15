
import speech_recognition as sr
import glob

class audio2s:
    def __init__(self,make):
        self.make = make
        print(sr.__version__)
        r = sr.Recognizer()

        for path in glob.glob("audio/*.mp3"):
            file_audio = sr.AudioFile(path)

            with file_audio as source:
                audio_text = r.record(source)

        print(type(audio_text)) 
        print(r.recognize_google(audio_text))
        '''print(f'Time taken {time.time()-start_time}s') '''