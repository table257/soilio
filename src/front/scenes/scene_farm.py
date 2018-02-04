import curses, time
from .scene import Scene
from ..dialogues.dialogue_buy import DialogueBuy

class SceneFarm:
    def __init__(self, screen):
        self.screen = screen
        self.sel = 0
        self.plots = []
        for i in range(484):
            self.plots.append(None)

    def load(self):
        self.draw_everything()

    def draw_plot(self, index, character, color_number):
        self.screen.addstr((index//30+1)*2, (index%30+1)*2+8, character, curses.color_pair(color_number))

    def draw_plots(self):
        for i in range(300):
            self.draw_plot(i, "_", 1)

    def draw_everything(self):
        self.screen.clear()
        self.screen.addstr(23, 1, "arrow keys: move, i: inspect, p: plant, h: harvest, b: buy, s: sell, q: quit".ljust(78), curses.color_pair(1))
        self.draw_plots()
        self.screen.refresh()

    def update(self):
        self.draw_plots()
        while True:
            self.draw_plot(self.sel, "_", 2)
            self.screen.refresh()
            ch = self.screen.getch()
            last_pressed = ch
            if (last_pressed == curses.KEY_DOWN):
                last_pressed = "down"
            elif (last_pressed == curses.KEY_UP):
                last_pressed = "up"
            elif (last_pressed == curses.KEY_LEFT):
                last_pressed = "left"
            elif (last_pressed == curses.KEY_RIGHT):
                last_pressed = "right"
            elif (last_pressed == ord('i')):
                last_pressed = "inspect"
            elif (last_pressed == ord('p')):
                last_pressed = "plant"
            elif (last_pressed == ord('h')):
                last_pressed = "harvest"
            elif (last_pressed == ord('b')):
                last_pressed = "buy"
            elif (last_pressed == ord('s')):
                last_pressed = "sell"
            elif (last_pressed == ord('q')):
                last_pressed = "quit"
            else:
                last_pressed = " "
            self.screen.addstr(22, 1, last_pressed.ljust(78), curses.color_pair(1))
            self.draw_plots()
            if (ch == curses.KEY_DOWN):
                self.sel = self.sel + 30
                if (self.sel > 299):
                    self.sel = 299
            elif (ch == curses.KEY_UP):
                self.sel = self.sel - 30
                if (self.sel < 0):
                    self.sel = 0
            elif (ch == curses.KEY_RIGHT):
                self.sel = self.sel + 1
                if (self.sel > 299):
                    self.sel = 299
            elif (ch == curses.KEY_LEFT):
                self.sel = self.sel - 1
                if (self.sel < 0):
                    self.sel = 0
            elif (ch == ord('b')):
                buy = DialogueBuy(curses.newwin(20, 40, 2, 20))
                buy.load()
                buy.update()
                buy.unload()
                self.draw_everything()
            elif (ch == ord('q')):
                self.screen.addstr(22, 1, "quitting...".ljust(78), curses.color_pair(1))
                self.screen.refresh()
                time.sleep(0.25)
                return 0

    def unload(self):
        self.screen.clear()
        self.screen.refresh()