from entry import Entry
from fasthtml.common import *

class EntryElement:
    def __init__(self, entry: Entry):
        self.entry = entry

    def getHtml(self):
        return Div(
            Img(src=self.entry.img, alt=self.entry.title),
            H2(self.entry.title),
            P(self.entry.text),
            A("Source", href=self.entry.source),
            A("Link", href=self.entry.link)
        )