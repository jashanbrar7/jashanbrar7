import curses
from curses import wrapper # takes over the terminal to use commands
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Welcome to the Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    key = stdscr.getkey()
    return key
    

def display_text(stdscr , target, current, wpm=0):        
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(2)
        if char!= correct_char:
            color = curses.color_pair(1)

        stdscr.addstr(0, i, char,  color) 




def wpm_test(stdscr):
    target_text = "Hello world"
    current_text= []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    # stdscr.clear()
    # stdscr.addstr(target_text)
    # stdscr.refresh()
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)



        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)    
        stdscr.refresh() 

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break


        try:
            key = stdscr.getkey()
        except:
            continue
        if key == '\x1b':
            break
        
        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
        



def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
    
        stdscr.addstr(2, 0, "Challenge Completed") 
        key = stdscr.getkey()                                                                                                               #stdscr.addstr(f"You pressed: {key}")
        if key == '\x1b':
            break                                                                                                           #stdscr.getch()
print(wrapper(main))
