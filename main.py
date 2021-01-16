import curses, wikipedia

""" 

This code displays the wikipedia page for python in a terminal window.

"""
currentPage = "Python (programming langauge)"

page=wikipedia.page(currentPage, None, True, True, True)
text=page.content


screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def infobar(currentInfoBar, page, section):
    num_rows, num_cols = screen.getmaxyx()
    while len(currentInfoBar) < num_cols:
        currentInfoBar += " "
    return currentInfoBar

screen.addstr(0, 0, infobar("This is the current infobar", None, None), curses.A_STANDOUT)
screen.addstr(1, 0, page.summary)

screen.refresh()
curses.napms(4000)

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()

print(text)
print(len(text))