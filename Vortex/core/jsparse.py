# external imports
import pyjsparser


class VortexJSParser:
    """
    VortexJSParser

    A class to parse javascript code.
    """

    def __init__(self):
        """
        __init__

        Initialize the parser.

        return: self
        """

    @staticmethod
    def parse(js_code):
        """
        parse

        Parse the javascript code.

        js_code: The javascript code.

        return: dict
        """
        return pyjsparser.parse(js_code)  # parse the javascript code
