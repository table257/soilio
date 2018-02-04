import curses
from .scene import Scene

class SceneMenu(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.sel = 0
        self.options = ["continue", "play game", "quit game"]

    def load(self):
        self.screen.clear()
        self.screen.addstr(1, 1, "soil.io v0.0.0".ljust(78), curses.color_pair(3))
        self.screen.addstr(2, 1, "a farming simulator with no romance by table257".ljust(78), curses.color_pair(1))
        self.screen.addstr(5, 1, "play game".ljust(78), curses.color_pair(1))
        self.screen.addstr(6, 1, "quit game".ljust(78), curses.color_pair(1))
        self.screen.addstr(23, 1, "arrow keys: move, space bar: select".ljust(78), curses.color_pair(1))
        self.screen.refresh()

    def update(self):
        while True:
            for i in range(len(self.options)):
                self.screen.addstr(5+i, 1, (" " + self.options[i]).ljust(78), curses.color_pair(1))
            self.screen.addstr(5+self.sel, 1, ("*" + self.options[self.sel]).ljust(78), curses.color_pair(2))
            self.screen.refresh()
            ch = self.screen.getch()
            if (ch == curses.KEY_DOWN):
                self.sel = self.sel + 1
                if (self.sel >= len(self.options)):
                    self.sel = len(self.options) - 1
            elif (ch == curses.KEY_UP):
                self.sel = self.sel - 1
                if (self.sel < 0):
                    self.sel = 0
            elif (ch == ord(' ')):
                if (self.sel == 0 or self.sel == 1):
                    return 1
                else:
                    return -1
    
    def unload(self):
        self.screen.clear()
        self.screen.refresh()