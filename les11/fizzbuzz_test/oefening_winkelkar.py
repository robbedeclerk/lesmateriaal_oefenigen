
class CannotAddItemWithoutPriceError(Exception):
    def __init__(self,message='you cannot add item without a price'):
        self.message=message
        super().__init__(self.message)

class Checkout:
    def __init__(self):
        self.prices ={}
        self.discounts={}
        self.items={}
        self.total = 0
    
    def add_item_price(self,item,price):
        self.prices[item]=price
        print(self.prices)
    
    def add_item(self,item):
        if self.prices.get(item,False):
            if item in self.items:
                self.items[item]+=1
            else:
                self.items[item]=1
            print(self.items)
        else:
            raise CannotAddItemWithoutPriceError
    
    def calculate_total(self):
        for item,number in self.items.items():
            if item in self.discounts:
                qty=self.discounts[item]['qty']
                qty_for_price= self.discounts[item]['qty_for_price']
                times_discounted_price= number //qty
                item_full_price= number % qty
                total += (times_discounted_price* qty_for_price+ item_full_price)*self.prices[item]
            else:
                total+= number*self.prices[item]
            print(item,number)
        return 7
    
    def add_discount_rule(self,item,qty,qty_for_price):
        self.discounts[item]={'qty':qty,
                              'qty_for_price':qty_for_price}