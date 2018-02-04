import curses
from .dialogue import Dialogue

class DialoguePlant(Dialogue):
    def __init__(self, window, inventory):
        super().__init__(window)
        self.inventory = inventory
        self.lookup = []
        self.sel = 0

    def load(self):
        count = 0
        for species in self.inventory:
            self.lookup[count] = species
            count = count + 1
        self.window.keypad(True)
        self.window.clear()
        self.window.border()
        self.draw_title()
        self.draw_inventory()
        self.draw_help()
        self.window.refresh()

    def draw_title(self):
        self.window.addstr(1, 2, "select seed to plant".ljust(36), curses.color_pair(1))

    def draw_help(self):
        self.window.addstr(16, 2, "space bar: select".ljust(36), curses.color_pair(1))
        self.window.addstr(17, 2, "up/down: move".ljust(36), curses.color_pair(1))
        self.window.addstr(18, 2, "q: quit".ljust(36), curses.color_pair(1))
    
    def draw_inventory(self):
        if (len(self.inventory) == 0):
            return
        for i in range(len(self.lookup)):
            self.window.addstr(3+i, 2, str(self.inventory[self.lookup[i]]).center(3), curses.color_pair(1))
            self.window.addstr(3+i, 5, self.lookup[i].name, curses.color_pair(1))
        self.window.addstr(3+self.sel, 2, str(self.inventory[self.lookup[self.sel]]).center(3), curses.color_pair(2))
        self.window.addstr(3+self.sel, 5, self.lookup[self.sel].name, curses.color_pair(2))
    
    def update(self):
        while True:
            self.draw_inventory()
            self.window.refresh()
            ch = self.window.getch()
            if (ch == curses.KEY_DOWN and len(self.inventory) > 0):
                self.sel = self.sel + 1
                if (self.sel >= len(self.lookup)):
                    self.sel = len(self.lookup) - 1
            elif (ch == curses.KEY_UP and len(self.inventory) > 0):
                self.sel = self.sel - 1
                if (self.sel < 0):
                    self.sel = 0
            elif (ch == ord(" ")):
                self.choice = self.lookup[self.sel]
            elif (ch == ord("q")):
                return 0

    def get_choice(self):
        return self.choice

    def unload(self):
        self.window.keypad(False)
        self.window.clear()
        self.window.refresh()
        del self.window