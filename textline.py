"""
Manages a single line of text,
"""


class Textline():

    def __init__(self, contents: str) -> None:
        """
        creates a texline object containing a line of text

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
                tempLine.contents = tempLine.contents + "1"
            print("Howdy, homeslice")
            return(tempLine.contents)
