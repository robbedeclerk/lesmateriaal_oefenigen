from abc import abstractmethod,ABC

@abstractmethod
class taxpayer:
    def __init__(self,salarys,):
        self.salarys=salarys
    
    @abstractmethod
    def calculate_tax():...


class studenttaxpayer(taxpayer):
    def salarys(values):
        x=values
    
    def calculate_tax(x):
        tax=x-(x/100*15)
        return(f'je tax is {tax}')


max=studenttaxpayer(4000)