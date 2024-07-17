import os

import speech_recognition as sr
import sounddevice

from src.speech_text import recognize_speech_from_mic

from src.command_mapping import COMMAND_MAPPINGS
from src.command_func_mappings import (COMMAND_FUNC_MAPPINGS, COMMAND_OBJ)
from utils.commands import Commands

class Pipeline():
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def get_matching_command(self, said_command):
        command = ''
        for key, value in COMMAND_MAPPINGS.items():
            if key in said_command:
                func_to_run = COMMAND_FUNC_MAPPINGS[value]
                command = func_to_run(said_text=said_command)
                break
        return command
    
    def execute_command(self, command):
        os.system(command)
        print(f"{command=}")
        print("Command Executed!")
        return

    def start_pipeline(self):
        voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
        said_command = voice_dict['alternative'][0]['transcript']
        print(f"{said_command=}")
        command = self.get_matching_command(said_command)
        self.execute_command(command)
        if said_command == 'exit':
            exit()

if __name__ == '__main__':
    pipeline_obj = Pipeline()
    pipeline_obj.start_pipeline()