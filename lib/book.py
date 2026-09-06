#!/usr/bin/env python3

class Book:
    def __init__(self, title: str, page_count: int):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self) -> int:
        return self._page_count

    @page_count.setter
    def page_count(self, value: int):
        if isinstance(value, int) and not isinstance(value, bool):
            self._page_count = value
        else:
            print("page_count must be an integer")
            self._page_count = None

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    
        