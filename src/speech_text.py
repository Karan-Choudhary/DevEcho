# r = sr.Recognizer()

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    """
    print("Say something!")
    while True:
        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)
                said_text = recognizer.recognize_google(audio, language='en-IN', show_all=True)
                print(f"{said_text=}")
                return said_text
        except Exception:
            print("Something went wrong! Please try again")


if __name__ == "__main__":
    # recognize_speech_from_mic(r, sr.Microphone())
    raise Exception("This file is not meant to run by itself.")