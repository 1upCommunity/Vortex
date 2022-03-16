from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ret = []

    def handle_starttag(self, tag, attrs):
        self.ret.append({"tag": tag, "attrs": attrs, "close": False})

    def handle_endtag(self, tag):
        self.ret.append({"tag": tag, "close": True})

    def handle_data(self, data):
        self.ret.append({"data": data})

class VortexHTMLParser:
    def __init__(self):
        pass

    def parse(self, html_code):
        parser = Parser()
        parser.feed(html_code)
        ret = parser.ret
        del parser
        return ret
