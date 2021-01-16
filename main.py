import curses, wikipedia

""" 

This code displays the wikipedia page for python in a terminal window.

"""

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

curses.napms(4000)

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()