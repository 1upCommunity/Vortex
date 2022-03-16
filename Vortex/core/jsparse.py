import pyjsparser

class VortexJSParser:
    def __init__(self):
        pass

    def parse(self, js_code):
        return pyjsparser.parse(js_code)
