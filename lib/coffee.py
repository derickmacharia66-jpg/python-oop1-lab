#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float | int):
        self.size = size
        self.price = price

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str):
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print('size must be Small, Medium, or Large')
            self._size = None

    def tip(self):
        print("This coffee is great, here's a tip!")
        if self.price is not None:
            self.price += 1
    