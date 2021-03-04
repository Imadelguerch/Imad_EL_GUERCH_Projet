#!/usr/bin/env python3

from functools import total_ordering

@total_ordering

class Book :
    def __init__(self ,name,):
        
        list_buy
        list_sell
        
    
    def insert_Order(self, quantity, price, buy=True):
        
    
    

        
        
class Order:
    def __init__(self, quantity, price, buy=True):
        self.__quantity = quantity
        self.price = price
        self.buy = buy
    def is_sell(self):
        return not self.buy
    
    def quantity(self):
        return self.__quantity if self.buy else -self.__quantity
    
    def __str__(self): # human-readable content
        return "%s @ %s" % (self.quantity, self.price)
    def __repr__(self): # unambiguous representation of the object
        return "Order(%s, %s)" % (self.quantity, self.price)
    
    def __eq__(self, other): # self == other
        return other and self.quantity == other.quantity and self.price == other.price
    def __lt__(self, other): # self < other
        return other and self.price < other.price