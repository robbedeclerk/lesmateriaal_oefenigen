class EmptyStringError(Exception):
    def __init__(self,message="u mag geen adress aanmaken met lege velden"):
        self.message=message
        super().__init__(self.message)