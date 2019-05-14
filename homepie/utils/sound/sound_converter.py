from pydub import AudioSegment


def mp3_to_wav(mp3path, wav_dest):
    sound = AudioSegment.from_mp3(mp3path)
    sound.export(wav_dest, format="wav")
