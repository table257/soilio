import curses
import time, traceback
import scenes

class SceneLoader:
    def __init__(self):
        self.screen = curses.initscr()
        self.scenes_list = []

    def load(self):
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.curs_set(0)
        self.screen.keypad(True)
        self.screen.clear()
        size = self.screen.getmaxyx()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        if (size[0] < 24 or size[1] < 80):
            self.screen.addstr(1, 1, "Screen too small: needs 80x24 minimum.", curses.color_pair(1))
            self.screen.refresh()
            time.sleep(2)
            unload()
        self.scenes_list.append(scenes.SceneMenu(self.screen))
        self.scenes_list.append(scenes.SceneFarm(self.screen))
        scene_index = 0
        while scene_index != -1:
            self.scenes_list[scene_index].load()
            new_scene_index = self.scenes_list[scene_index].update()
            self.scenes_list[scene_index].unload()
            scene_index = new_scene_index

    def unload(self):
        self.screen.keypad(False)
        curses.curs_set(1)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def run(self):
        try:
            self.load()
            self.unload()
            return 0
        except Exception:
            self.screen.clear()
            self.screen.addstr(1, 1, "something bad happened and we're crashing in 5 seconds!", curses.color_pair(1))
            self.screen.addstr(2, 1, traceback.format_exc(), curses.color_pair(2))
            curses.beep()
            self.screen.refresh()
            time.sleep(5)
            self.unload()
            return -1