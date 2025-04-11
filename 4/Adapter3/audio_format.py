class AudioPlayer:
    def play(self, filename, format):
        pass

class WAVPlayer(AudioPlayer):
    def play(self, filename, format):
        if format == "wav":
            print(f"Lejátszás WAV-ban: {filename}")
        else:
            print(f"A formátum nem támogatott: {format}")

class MP3Player:
    def play_mp3(self, filename):
        print(f"Lejátszás MP3-ban: {filename}")

class FLACPlayer:
    def play_flac(self, filename):
        print(f"Lejátszás FLAC-ben: {filename}")

class AudioAdapter(AudioPlayer):
    def __init__(self, player):
        self.player = player

    def play(self, filename, format):
        if format == "mp3":
            self.player.play_mp3(filename)
        elif format == "flac":
            self.player.play_flac(filename)
        else:
            print(f"A formátum nem támogatott: {format}")


wav_player = WAVPlayer()
wav_player.play("song2.wav","mp3")

mp3_player = AudioAdapter(MP3Player())
flac_player = AudioAdapter(FLACPlayer())

wav_player.play("song.wav", "wav")
mp3_player.play("song.mp3", "mp3")
flac_player.play("song.flac", "flac")
