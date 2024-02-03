from typing import Protocol

class shape(Protocol):
    def render(self) -> str:...
    def area(self)-> float:...


class symentry(Protocol):
    def angle(self)->float:...

class skewable(Protocol):
    def points(self)-> int:...


class circle:
    def render(self) -> str:
        return('circle geametry')
    def area(self)-> float:
        return 42.0


class star:
    def render(self) -> str:
        return('star geametry')
    def area(self)-> float:
        return 50.0
    def points(self)-> int:
        return 5

class parralelagom:
    def render(self) -> str:...
    def area(self)-> float:...
    def angle(self)->float:...