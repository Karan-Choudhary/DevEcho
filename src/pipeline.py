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
        
    def refactor_additional_details(self):
        speak('Please Provide variable current name: ')
        voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
        current_name = voice_dict['alternative'][0]['transcript']
        # current_name = str(input("Enter old name: ")).lower()
        print(f"{current_name=}")
        speak('Please Provide variable new name: ')
        voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
        new_name = voice_dict['alternative'][0]['transcript']
        # new_name = str(input("Enter new name: ")).lower()
        print(f"{new_name=}")
        speak('Do you want to change all files?')
        voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
        all_files = voice_dict['alternative'][0]['transcript']
        # all_files = str(input("yes or no: ")).lower()
        if all_files.lower().strip() != 'yes':
            speak('Please provide file names: ')
            voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
            file_name = voice_dict['alternative'][0]['transcript']
            # file_name = str(input("Enter command: ")).lower()
            print(f"{file_name=}")
            all_files = file_name
        return {
            'old_name': current_name,
            'new_name': new_name,
            'file_name': all_files,
        }

    def get_matching_command(self, said_command):
        command_idx, command_label = self.predict(said_command)
        print(f"{command_idx=}")
        print(f"{command_label=}")
        if command_idx == 7:
            additional_data = self.refactor_additional_details()
        else:
            additional_data = {}
        func_to_run = DYNAMIC_FUNC_MAPPINGS[command_idx]
        return func_to_run(said_text=said_command, additional_data=additional_data)
    
    def execute_command(self, command):
        os.system(command)
        print(f"{command=}")
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
            # said_command = str(input("Enter command: ")).lower()
            voice_dict = recognize_speech_from_mic(self.recognizer, self.mic)
            said_command = voice_dict['alternative'][0]['transcript']
            if said_command == 'exit':
                exit()
            print(f"{said_command=}")
            command = self.get_matching_command(said_command)
            self.execute_command(command)

if __name__ == '__main__':
    pipeline_obj = Pipeline()
    pipeline_obj.start_pipeline()