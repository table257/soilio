import curses, time
from .dialogue import Dialogue

class DialogueSave(Dialogue):
    def __init__(self, window):
        super().__init__(window)
        self.letters = ['a', 'a', 'a', 'a', 'a']
        self.sel = 0

    def load(self):
        self.window.keypad(True)
        self.window.clear()
        self.window.border()
        self.window.addstr(1, 2, "what's your name?".center(56), curses.color_pair(1))
        self.draw_name(1)
        self.window.addstr(5, 2, "up/down: cycle, left/right: move, space bar: accept".center(56), curses.color_pair(1))
        self.window.refresh()

    def draw_name(self, color):
        self.window.addstr(3, 2, "".join(self.letters).center(56), curses.color_pair(color))

    def flash_name(self, duration, times):
        for i in range(times):
            self.draw_name(2)
            self.window.refresh()
            time.sleep(duration)
            self.draw_name(1)
            self.window.refresh()
            time.sleep(duration)
    
    def update(self):
        while True:
            self.draw_name(1)
            self.window.addstr(3, 2+25+self.sel, self.letters[self.sel], curses.color_pair(2))
            self.window.refresh()
            ch = self.window.getch()
            if (ch == curses.KEY_DOWN):
                self.letters[self.sel] = chr(ord(self.letters[self.sel]) + 1)
                if (self.letters[self.sel] > 'z'):
                    self.letters[self.sel] = 'a'
            elif (ch == curses.KEY_UP):
                self.letters[self.sel] = chr(ord(self.letters[self.sel]) - 1)
                if (ord(self.letters[self.sel]) < ord('a')):
                    self.letters[self.sel] = 'z'
            elif (ch == curses.KEY_RIGHT):
                self.sel = self.sel + 1
                if (self.sel >= len(self.letters)):
                    self.sel = len(self.letters) - 1
            elif (ch == curses.KEY_LEFT):
                self.sel = self.sel - 1
                if (self.sel < 0):
                    self.sel = 0
            elif (ch == ord(' ')):
                self.flash_name(0.2, 3)
                return 0
    
    def unload(self):
        self.window.keypad(False)
        self.window.clear()
        self.window.refresh()
        del self.window
    
    def get_name(self):
        return "".join(self.letters)