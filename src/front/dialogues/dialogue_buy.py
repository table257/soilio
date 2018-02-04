import curses
from .dialogue import Dialogue
import time

class DialogueBuy(Dialogue):
    def __init__(self, window, species_list):
        super().__init__(window)
        self.species_list = species_list
        self.shopping = {}
        for species in self.species_list:
            self.shopping[species] = 0
        self.sel = 0

    def load(self):
        self.window.keypad(True)
        self.window.clear()
        self.window.border()
        self.draw_title()
        self.draw_list()
        self.draw_help()
        self.window.refresh()

    def draw_title(self):
        self.window.addstr(1, 2, "buy things!".ljust(36), curses.color_pair(1))

    def draw_help(self):
        self.window.addstr(16, 2, "left/right: change amt.".ljust(36), curses.color_pair(1))
        self.window.addstr(17, 2, "up/down: move".ljust(36), curses.color_pair(1))
        self.window.addstr(18, 2, "q: quit".ljust(36), curses.color_pair(1))
    
    def draw_list(self):
        if (len(self.species_list) == 0):
            return
        for i in range(len(self.species_list)):
            if (i > 10):
                break # we dont have scrolling
            self.window.addstr(3+i, 2,
                " "+str(self.shopping[self.species_list[i]]).center(3)+" ", curses.color_pair(1))
            self.window.addstr(3+i, 7,
                " x "+self.species_list[i].name.ljust(28), curses.color_pair(1))
        self.window.addstr(3+self.sel, 2,
            "-"+str(self.shopping[self.species_list[self.sel]]).center(3)+"+", curses.color_pair(2))
        self.window.addstr(3+self.sel, 7,
            " x "+self.species_list[self.sel].name.ljust(28), curses.color_pair(2))
    
    def update(self):
        while True:
            self.draw_list()
            self.window.refresh()
            ch = self.window.getch()
            if (ch == curses.KEY_DOWN and len(self.species_list) > 0):
                self.sel = self.sel + 1
                if (self.sel >= len(self.species_list)):
                    self.sel = len(self.species_list) - 1
            elif (ch == curses.KEY_UP and len(self.species_list) > 0):
                self.sel = self.sel - 1
                if (self.sel < 0):
                    self.sel = 0
            elif (ch == curses.KEY_LEFT and len(self.species_list) > 0):
                self.shopping[self.species_list[self.sel]] = self.shopping[self.species_list[self.sel]] - 1
                if (self.shopping[self.species_list[self.sel]] < 0):
                    self.shopping[self.species_list[self.sel]] = 0
            elif (ch == curses.KEY_RIGHT and len(self.species_list) > 0):
                self.shopping[self.species_list[self.sel]] = self.shopping[self.species_list[self.sel]] + 1
            elif (ch == ord("q")):
                return 0

    def get_shopping(self):
        return self.shopping

    def unload(self):
        self.window.keypad(False)
        self.window.clear()
        self.window.refresh()
        del self.window