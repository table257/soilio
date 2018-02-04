import curses, time
from .scene import Scene

class SceneFarm:
    def __init__(self, screen):
        self.screen = screen
        self.sel_x = 1
        self.sel_y = 1
        self.plots = []
        for i in range(484):
            self.plots.append(None)

    def draw_plot(self, index, character, color_number):
        self.screen.addstr((index//30+1)*2, (index%30+1)*2, character, curses.color_pair(color_number))
    
    def redraw_plots(self):
        for i in range(300):
            self.draw_plot(i, "_", 1)

    def update(self):
        self.redraw_plots()
        while True:
            self.screen.addstr(self.sel_y*2, self.sel_x*2, "_", curses.color_pair(2))
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
            elif (last_pressed == ord(' ')):
                last_pressed = "select"
            else:
                last_pressed = " "
            self.screen.addstr(22, 1, last_pressed.ljust(78), curses.color_pair(1))
            self.redraw_plots()
            if (ch == curses.KEY_DOWN):
                self.sel_y = self.sel_y + 1
                if (self.sel_y > 10):
                    self.sel_y = 10
            elif (ch == curses.KEY_UP):
                self.sel_y = self.sel_y - 1
                if (self.sel_y < 1):
                    self.sel_y = 1
            elif (ch == curses.KEY_RIGHT):
                self.sel_x = self.sel_x + 1
                if (self.sel_x > 30):
                    self.sel_x = 30
            elif (ch == curses.KEY_LEFT):
                self.sel_x = self.sel_x - 1
                if (self.sel_x < 1):
                    self.sel_x = 1
            elif (ch == ord('q')):
                self.screen.addstr(22, 1, "quitting...".ljust(78), curses.color_pair(1))
                self.screen.refresh()
                time.sleep(0.5)
                return 0

    def load(self):
        self.screen.clear()
        self.screen.addstr(23, 1, "arrow keys: move, q: quit".ljust(78), curses.color_pair(1))
        self.screen.refresh()

    def unload(self):
        self.screen.clear()
        self.screen.refresh()