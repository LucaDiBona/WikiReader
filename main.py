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

def infobar(page, section):
    num_rows, num_cols = screen.getmaxyx()
    infoBar = page + " | " + section
    while len(infoBar) < num_cols:
        infoBar += " "
    if len(infoBar) > num_cols:
        abbrvLength = num_cols + len(section) - len(infoBar) - 3        #appropriate length for new section to display (not including ...)
        abbrvSection = section[:abbrvLength]
        abbrvSection += "..."
        infoBar = infobar(page, abbrvSection)
    return infoBar

screen.addstr(0, 0, infobar(currentPage, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."), curses.A_STANDOUT)
screen.addstr(1, 0, page.summary)
screen.addstr(0,0,"")
screen.refresh()
curses.napms(4000)

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()

##print(text)
##print(len(text))