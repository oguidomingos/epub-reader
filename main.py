'''
This is the main file for the EPUB audio player application. It initializes the application and handles the GUI.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
import ebooklib
from ebooklib import epub
from gtts import gTTS
from bs4 import BeautifulSoup
import os
import logging
from player import Player
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.load = tk.Button(self)
        self.load["text"] = "Load EPUB"
        self.load["command"] = self.load_epub
        self.load.pack(side="top")
        self.play = tk.Button(self)
        self.play["text"] = "Play"
        self.play["command"] = self.play_audio
        self.play.pack(side="top")
        self.pause = tk.Button(self)
        self.pause["text"] = "Pause"
        self.pause["command"] = self.pause_audio
        self.pause.pack(side="top")
        self.stop = tk.Button(self)
        self.stop["text"] = "Stop"
        self.stop["command"] = self.stop_audio
        self.stop.pack(side="top")
    def load_epub(self):
        try:
            file_path = filedialog.askopenfilename()
            book = epub.read_epub(file_path)
            text = ''
            for item in book.get_items():
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                    html_content = item.get_content().decode('utf-8')
                    soup = BeautifulSoup(html_content, 'html.parser')
                    text += soup.get_text()
            self.player = Player(text)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
    def play_audio(self):
        if hasattr(self, 'player'):
            self.player.play()
        else:
            messagebox.showerror("Error", "No EPUB file loaded")
    def pause_audio(self):
        if hasattr(self, 'player'):
            self.player.pause()
        else:
            messagebox.showerror("Error", "No EPUB file loaded")
    def stop_audio(self):
        if hasattr(self, 'player'):
            self.player.stop()
        else:
            messagebox.showerror("Error", "No EPUB file loaded")
root = tk.Tk()
app = Application(master=root)
app.mainloop()