import random
import string
from fasthtml.common import *

from entry import Entry
from entryElement import EntryElement

app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML", P("Let's do this!"))

@rt("/list")
def get():
    letters = random.choices(string.ascii_uppercase, k=random.randint(5, 20))

    entries = []
    for i in range(1, 4):
        entries.append(Entry(title = "Title " + str(i), text = "Text " + str(i), source = "Source " + str(i), link = "https://www.google.de/", img = "https://via.placeholder.com/150"))

    items = [EntryElement(i).getHtml() for i in entries]

    return Titled("Entries",
        Ul(*items)
    )

serve()