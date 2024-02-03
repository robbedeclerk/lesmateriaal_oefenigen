from .errors import *
import sys
print(sys.path)


class Address:
    def __init__(self, street,city,zip_code,country):
        self.street=street
        self.city=city
        self.zip_code=zip_code
        self.country=country
    def __str__(self):
        return f"{self.street},{self.city},{self.zip_code},{self.country}"
    
    
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self,value):
        if value == "":
            raise EmptyStringError()
        self.__street = value
        