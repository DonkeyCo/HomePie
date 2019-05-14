import simpleaudio as sa
import threading
import time


def play_sound(location):
    t1 = threading.Thread(target=play, args=[location])
    t2 = threading.Thread(target=stop_sound)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def play(location):
    wave_obj = sa.WaveObject.from_wave_file(location)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def stop_sound():
    time.sleep(10)
    sa.stop_all()
