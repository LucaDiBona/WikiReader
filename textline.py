"""
Manages a single line of text
"""


class Textline():

    def __init__(self, contents: str) -> None:
        """
        creates a textline object containing a line of text

        Args:
            contents (str): the contents of the textline
        """
        self._contents = contents
        # minimum output length

    @property
    def contents(self) -> str:
        """
        getter for the full contents of the textline as a string
        """
        return(self._contents)

    @contents.setter
    def contents(self, value: str) -> None:
        """
        setter for the full contents of the textline

        Args:
            value (str): the new value for contents
        """
        self._contents = value

    # TODO allow selection of where extra spaces & ... to be placed
    def output(self, minLength: int = 0, maxLength=None) -> str:
        """
        produces an output textline

        Args:
            minLength (int, optional): The minimum length of the output textline that will be provided. Defaults to 0.
            maxLength (None or int, optional): The maximum length of the output textline that will be provided. If None, will not adjust to a specific length. Defaults to None.

        Returns:
            str: the output textline. If minLength > maxLength, will return "Error: minLength must be less than maxLength"
        """
        tempLine = Textline(self._contents)
        if maxLength != None:
            if minLength > maxLength:
                return("Error: minLength must be less than maxLength")
            elif len(self._contents) > maxLength:
                return(self._contents[:(maxLength-3)]+"...")
            elif len(self._contents) == maxLength:
                return(self._contents)
            else:
                return(tempLine.output(minLength))
        else:
            while len(tempLine.contents) < minLength:
                tempLine.contents = tempLine.contents + " "
            return(tempLine.contents)


class Title(Textline):

    def __init__(self, contents: str) -> None:
        """
        Creates a title object containing the page title and the maximum length of this that will be displayed

        Args:
            contents (str): the title of the page to be displayed
        """
        super().__init__(contents)

    def output(self,minLength:int =0, maxLength: int = None) -> str:
        """
        Outputs the title

        Args:
            maxLength (int, optional): The maximum length of the title that will be ouput. If None, no maximum length. Defaults to None.

        Returns:
            str: the output
        """
        return(super().output(minLength, maxLength))


class SectionTitle(Title):

    def __init__(self, sectionName: str, sectionNumber: int = 0) -> None:
        """
        Creates a section header

        Args:
            sectionName (str): The full text of the section name
            sectionNumber (int, optional): The number of the section. Defaults to 0.
        """
        self._sectionNumber=sectionNumber
        self._sectionName=sectionName
        self._contents=""
        super().__init__(self._contents)

    @property
    def sectionName(self) -> str:
        """
        getter for the full contents of the header title as a string
        """
        return(self._sectionName)

    @sectionName.setter
    def sectionName(self, value: str) -> None:
        """
        setter for the change of header title

        Args:
            value (str): the new value for contents
        """
        self._sectionName = value
        self.update()

    def output(self, maxLength:int, minLength:int =0) -> str:
        """
        Generates output text for the section titlebar

        Args:
            maxLength (int): maximum Length of the section titlebar
            minLength (int, optional): Minimum length of the section titlebar. Defaults to 0.

        Returns:
            str: text for the titlebar
        """
        self._contents = "[" + str(self._sectionNumber) + "] " + self._sectionName
        return(super().output(minLength, maxLength))
class cursorPos():
    """
    A marker showing the cursor's poisition
    """

    def __init__(self, line: int, col: int) -> None:
        """
        creates a set of coordinates

        Args:
            line (int): the line on which the cursor is
            col (int): the column that the cursor is in
        """
        self._contents=""
        super().__init__(self._contents)
        self._line=line
        self._col=col

    def output(self) -> str:
        """
        Provides the position of the cursor

        Returns:
            str: the position of the cursor
        """
        self._contents = str(self._line) + ", " + str(self._line)
        return(super().output(0, None))

class StatusBar(Textline):
    """
    a subclass of Textline that manages the StatusBar at the top of the window
    """

    def __init__(self, page: object, section: object, locator: object) -> None:
        """
        creates a StatusBar

        Args:
            page (object): the current page
            section (object): the current section
            locator (object): the position in the current section
        """
        super().__init__()
