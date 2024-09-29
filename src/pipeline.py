import os

import speech_recognition as sr
import sounddevice

from src.speech_text import speak, recognize_speech_from_mic
from src.command_func_mappings import (DYNAMIC_FUNC_MAPPINGS)
from utils.command_recognizer import CommandRecognizer


class Pipeline(CommandRecognizer):
    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.voice = 'en-AU-NatashaNeural'

    def get_matching_command(self, said_command):
        command_idx, command_label = self.predict(said_command)
        print(f"{command_idx=}")
        print(f"{command_label=}")
        func_to_run = DYNAMIC_FUNC_MAPPINGS[command_idx]
        return func_to_run(said_text=said_command)
    
    def execute_command(self, command):
        os.system(command)
        # print(f"{command=}")
        speak('command successfully executed!')
        return

    def start_pipeline(self):
        voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
        said_command = voice_dict['alternative'][0]['transcript']
        # said_command = str(input("Enter command: ")).lower()
        print(f"{said_command=}")
        if "wake up" in said_command or "hey" in said_command:
            speak('I am ready')
        while True:
            voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
            said_command = voice_dict['alternative'][0]['transcript']
            # said_command = str(input("Enter command: ")).lower()
            print(f"{said_command=}")
            command = self.get_matching_command(said_command)
            self.execute_command(command)
            if said_command == 'exit':
                exit()

if __name__ == '__main__':
    pipeline_obj = Pipeline()
    pipeline_obj.start_pipeline()