import curses
import time, traceback
import scenes

screen = curses.initscr()
scenes_list = []

def load():
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.curs_set(0)
    screen.keypad(True)
    screen.clear()
    size = screen.getmaxyx()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    if (size[0] < 24 or size[1] < 80):
        screen.addstr(1, 1, "Screen too small: needs 80x24 minimum.", curses.color_pair(1))
        screen.refresh()
        time.sleep(2)
        unload()
    scenes_list.append(scenes.SceneMenu(screen))
    scenes_list.append(scenes.SceneFarm(screen))
    scene_index = 0
    while scene_index != -1:
        scenes_list[scene_index].load()
        new_scene_index = scenes_list[scene_index].update()
        scenes_list[scene_index].unload()
        scene_index = new_scene_index

def unload():
    screen.keypad(False)
    curses.curs_set(1)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    exit(0)

try:
    load()
    unload()
except Exception:
    screen.clear()
    screen.addstr(1, 1, "something bad happened and we're crashing in 5 seconds!", curses.color_pair(1))
    screen.addstr(2, 1, traceback.format_exc(), curses.color_pair(2))
    curses.beep()
    screen.refresh()
    time.sleep(5)
    unload()