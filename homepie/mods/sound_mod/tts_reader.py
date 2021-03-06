import os
from gtts import gTTS
import homepie.utils.sound.sound_converter as convert
import homepie.mods.sound_mod.sound_processing as sp
import time


class Reader:

    def create_wav(self, text, language):
        obj = gTTS(text=text, lang=language)
        obj.save(os.path.join(os.getcwd(), "resources", "sounds", "tts", "news.mp3"))
        convert.mp3_to_wav((os.path.join(os.getcwd(), "resources", "sounds", "tts", "news.mp3")),
                           (os.path.join(os.getcwd(), "resources", "sounds", "tts", "news.wav")))

    def play(self):
        sp.play(os.path.join(os.getcwd(), "resources", "sounds", "tts", "news.wav"))
        self.clear()

    def next(self):
        time.sleep(10)
        sp.stop_sound()

    def clear(self):
        os.remove(os.path.join(os.getcwd(), "resources", "sounds", "tts", "news.wav"))
        os.remove(os.path.join(os.getcwd(), "resources", "sounds", "tts", "news.mp3"))
        print("Sound files removed...")
