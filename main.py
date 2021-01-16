import curses, wikipedia

""" 

This code displays the wikipedia page for python in a terminal window.

"""
text=wikipedia.summary("Python (programming langauge)")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

screen.addstr(0,0,text)

screen.refresh()
curses.napms(4000)

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()