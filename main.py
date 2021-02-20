import curses
import wikipedia

"""

This code displays the wikipedia page for python in a terminal window.


TODO:

[ ] Ensure window fits on screen
[ ] Add command line
[ ] Add commands to move sections
[ ] Add commands to view sources & footnotes
[ ] Add a way to follow external links (inc images)
[ ] Parse tables
[ ] Parse sidebars & other custom infoboxes
[ ] Bookmarks
[ ] History
[ ] Local downloads?
"""
currentPage = "Python (programming langauge)"

page = wikipedia.page(currentPage, None, True, True, True)
text = page.content


def isPunc(char):  # tests if an inputted character is punctuation
    punctuation = " -.?,!"
    for i in range(len(punctuation)):
        if char == punctuation[i]:
            return True
    return False


screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


# outputs an infobar, a sting of the form [current page] | [current section]
def infobar(page, section, ):
    num_rows, num_cols = screen.getmaxyx()
    infoBar = page + " | " + section
    while len(infoBar) < num_cols:
        infoBar += " "
    if len(infoBar) > num_cols:
        # appropriate length for new section to display (not including ...)
        abbrvLength = num_cols + len(section) - len(infoBar) - 3
        abbrvSection = section[:abbrvLength]
        abbrvSection += "..."
        infoBar = infobar(page, abbrvSection)
    return infoBar


# takes a str input and returns a list of strings arranged to fit nicely in the terminal window
def textProcess(inputStr):
    num_rows, num_cols =screen.getmaxyx()
    outputStr = ""
    outputList = []
    winHeight=num_rows-2
    lines = 0
    inputLen = len(inputStr)
    while len(outputStr) < inputLen:  # max length string displayed
        if len(inputStr) <=1:
            outputStr += inputStr
            break
        lineStr = inputStr[:num_cols + 1]
        if lineStr[0] == "":  # trims unnecessary spaces from beginning of lines colour
            lineStr = lineStr[0:]
        else:  # sets current line to new max size
            lineStr = lineStr[:len(lineStr) - 1]
        if len(lineStr) < len(inputStr) and len(lineStr) != 0:
            # there is a word going over multiple lines
            if not(inputStr[len(lineStr)] == " " or isPunc(lineStr[len(lineStr) - 1])):
                # shortens line until start of word found
                while not(isPunc(lineStr[len(lineStr) - 1]) or len(lineStr) == 1):
                    lineStr = lineStr[:len(lineStr) - 1]
        # removes processed line from temp string
        inputStr = inputStr[len(lineStr):]
        outputStr += lineStr
        lines += 1
    if lines<=winHeight:
        outputList.append(outputStr)
    else:
        pass
    return outputList


mainText = textProcess(page.summary)

screen.addstr(0, 0, infobar(currentPage, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."), curses.A_STANDOUT)

print(mainText)

screen.addstr(1, 0, mainText[0])
screen.refresh()
curses.napms(3000)

# print(textProcess(page.summary))

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
