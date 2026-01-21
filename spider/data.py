from dataclasses import dataclass

from bs4.element import PageElement


@dataclass
class PaiAppRawData:
    title: str
    html_elements: list[PageElement] | str


@dataclass
class PaiAppData:
    date: str
    title: str
    platforms: list[str]
    content: str
    img_list: list[str]
