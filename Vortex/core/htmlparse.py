# internal imports
from html.parser import HTMLParser


class Parser(HTMLParser):
    """
    Parser

    A class to parse HTML.
    """

    def __init__(self):
        """
        __init__

        Initialize the parser.

        return: self
        """
        super().__init__()  # initialize the base class
        self.ret = []  # the return value

    def handle_starttag(self, tag, attrs):
        """
        handle_starttag

        Handle the start of a tag.

        tag: The tag.
        attrs: The attributes.

        return: None
        """
        self.ret.append({"tag": tag, "attrs": attrs, "close": False}
                        )  # add the tag to the return value

    def handle_endtag(self, tag):
        """
        handle_endtag

        Handle the end of a tag.

        tag: The tag.

        return: None
        """
        self.ret.append({"tag": tag, "close": True}
                        )  # add the tag to the return value

    def handle_data(self, data):
        """
        handle_data

        Handle data like strings, etc.

        data: The data.

        return: None
        """
        self.ret.append({"data": data})  # add the data to the return value


class VortexHTMLParser:
    """
    VortexHTMLParser

    A class to parse HTML.
    """

    def __init__(self):
        """
        __init__

        Initialize the parser.

        return: self
        """

    @staticmethod
    def parse(html_code):
        """
        parse

        Parse the HTML code.

        html_code: The HTML code.

        return: list
        """
        parser = Parser()  # create the parser
        parser.feed(html_code)  # feed the parser
        ret = parser.ret  # get the return value
        return ret  # return the return value
