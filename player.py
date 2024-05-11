'''
This file handles the text-to-speech conversion and audio playback.
'''
from gtts import gTTS
from pygame import mixer
import os
import uuid
class Player:
    def __init__(self, text):
        self.text = text
        self.is_paused = False
        self.filename = f"audio_{uuid.uuid4()}.mp3"
        self.tts = gTTS(text=self.text, lang='pt')
        self.tts.save(self.filename)
        mixer.init()
        mixer.music.load(self.filename)
    def play(self):
        if self.is_paused:
            mixer.music.unpause()
            self.is_paused = False
        else:
            mixer.music.play()
    def pause(self):
        if not self.is_paused:
            mixer.music.pause()
            self.is_paused = True
    def stop(self):
        mixer.music.stop()
        self.is_paused = False
        if os.path.exists(self.filename):
            os.remove(self.filename)