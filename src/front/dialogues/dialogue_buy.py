import curses
from .dialogue import Dialogue
import time

class DialogueBuy(Dialogue):
    def __init__(self, window):
        self.window = window

    def load(self):
        self.window.clear()
        self.window.border()
        self.window.addstr(1, 1, "buy things!", curses.color_pair(1))
        self.window.refresh()
    
    def update(self):
        time.sleep(3)
        return 0

    def unload(self):
        self.window.clear()
        self.window.refresh()
        del self.window