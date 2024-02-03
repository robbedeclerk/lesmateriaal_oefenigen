from abc import abstractmethod,ABC
class voertuig(ABC):
    def __init__(self,merk,model):
        self.merk=merk
        self.model=model
    @abstractmethod
    def rijden():...
    
    def stoppen():...
    
    def wielen():...
    @abstractmethod
    def tanken():...

class fiets(voertuig):
    def __init__(self, merk, model):
        super().__init__(merk, model)
        merk= input('wat is het merk')
        model=input('wat is het merk')
    
    def rijden():...
    
    def stoppen():...
    
    def wielen():...



class auto(voertuig):
    def __init__(self, merk, model):
        super().__init__(merk, model)
        merk= input('wat is het merk')
        model=input('wat is het merk')
    
    def rijden():...
    
    def stoppen():...
    
    def wielen():...

class benzineauto(auto):
    def __init__(self, merk, model):
        super().__init__(merk, model)
        merk= input('wat is het merk')
        model=input('wat is het merk')
    
    def rijden():...
    
    def stoppen():...
    
    def wielen():...
    
    def tanken():...
