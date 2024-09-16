from pydantic import BaseModel, FileUrl, HttpUrl


class Entry(BaseModel):
    title: str
    text: str
    source: str
    link: HttpUrl = ""
    img: HttpUrl = ""