import speech_recognition as sr
import sounddevice

from speech_text import recognize_speech_from_mic


class Pipeline:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def start_pipeline(self):
        voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
        said_command = voice_dict['alternative'][0]['transcript']
        print(f"{said_command=}")
        
        if said_command == 'exit':
            exit()

if __name__ == '__main__':
    pipeline_obj = Pipeline()
    pipeline_obj.start_pipeline()