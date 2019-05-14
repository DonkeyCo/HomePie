import speech_recognition as sr


class Recognition:

    def __init__(self, config=None):
        self.config = config
        self.r = sr.Recognizer()

    def listen_background(self):
        self.r.listen_in_background(sr.Microphone(), self.get_text)

    def get_text(self, recognizer, audio):
        text = ""
        try:
            text = self.r.recognize_wit(audio, self.config["WIT"]["API_KEY"])
            if "okay home" in text:
                print(text)
            else:
                print("lol " + text)
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))
