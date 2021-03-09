#!/usr/bin/env python3

from functools import total_ordering

import pandas as pd

class Book() :
    def __init__(self ,name):
        
        self.name=name
        self.list_buy=[]
        self.list_sell=[]
        self.cpt=0
        
                       
    def insert_buy(self,q , p):
        self.cpt+=1
        O=Order(p,q)
        print("---Insert Buy",end=' ')
        O.set_id(self.cpt)
        print(repr(O) ," id= %d" % O.get_id()," on  %s"% self.name)
        print("")
        
        if(self.list_sell!=[] and p>=self.list_sell[0].price  ):     
            if(self.list_sell[0]==O):
                print("Execute %s at %s on %s" % (q,self.list_sell[0].price,self.name))
                del self.list_sell[0]      
            else:
                x=q
                while(x>0):
                    if(x<self.list_sell[0].quantity):
                        self.list_sell[0].quantity-=x
                        print("Execute %s at %s on %s" % (x,self.list_sell[0].price,self.name))
                        x=0
                    else:
                        print("Execute %s at %s on %s" % (self.list_sell[0].quantity,self.list_sell[0].price,self.name))
                        x-=self.list_sell[0].quantity
                        
                        del self.list_sell[0]
        else:
            self.list_buy.append(O)
            self.list_buy=sorted(self.list_buy,reverse=True)
        self.OrderBook()
        
    
    def insert_sell(self,q,p):
        self.cpt+=1
        O=Order(p,q)
        print("---Insert Sell ",end=' ')
        O.set_id(self.cpt)
        print(repr(O) ," id= %d" % O.get_id()," on  %s"% self.name)
        print("")
        
        if(self.list_buy!= [] and p<=self.list_buy[0].price):     
            if(self.list_buy[0]==O):
                print("Execute %s at %s on %s" % (q,self.list_buy[0].price,self.name))
                del self.list_buy[0]      
            else:
                x=q
                while(x>0):
                    if(x<self.list_buy[0].quantity):
                        self.list_buy[0].quantity-=x
                        print("Execute %s at %s on %s" % (x,self.list_buy[0].price,self.name))
                        x=0
                    else:
                        print("Execute %s at %s on %s" % (self.list_buy[0].quantity,self.list_buy[0].price,self.name))
                        x-=self.list_buy[0].quantity
                        
                        del self.list_buy[0]                                            
        
        else:
            self.list_sell.append(O)
            self.list_sell=sorted(self.list_sell)   
        self.OrderBook()   
                
       
        
    def ListBuy(self): 
        d_quantity=[]
        d_price=[]
        d_id=[]
        B=[]
        for i in range(len(self.list_buy)):
            B.append("Buy")
            d_quantity.append(self.list_buy[i].quantity)
            d_price.append(self.list_buy[i].price)
            d_id.append(self.list_buy[i].id)
            
        data = {'Quantity':d_quantity,'Price':d_price, "Id":d_id }
        df = pd.DataFrame(data, index=B)
        
        print(df)
        
    def ListSell(self): 
        d_quantity=[]
        d_price=[]
        d_id=[]
        S=[]
        for i in range(len(self.list_sell)):
            S.append("Sell")
            d_quantity.append(self.list_sell[i].quantity)
            d_price.append(self.list_sell[i].price)
            d_id.append(self.list_sell[i].id) 
        data = {'Quantity':d_quantity,'Price':d_price, "Id":d_id }
        df = pd.DataFrame(data, index=S)
        print(df)
                
    def OrderBook(self): 
          print("Book on %s" %self.name)
          if(self.list_sell!=[]):
              self.ListSell()
          print("------------------------")
          if(self.list_buy!=[]):
              self.ListBuy()
          print("------------------------")
          print(" ")
    

@total_ordering       
        
class Order:
    def __init__(self,price , quantity):
        self.quantity = quantity
        self.price = price
        self.id=0
        
    def is_Buy(self):
        return  self.buy
  
    def set_id(self,x):
       self.id+=x
    def get_id(self):
       return self.id
       
    def __str__(self):
        return "    %s @ %s  id= %d" % (self.quantity, self.price ,self.id)
        
    def __repr__(self): 
        return "Order(%s, %s)" % (self.quantity, self.price)
    
    def quantity(self):
        return self.quantity 
    
    def price(self):
        return self.price 
    
    def __eq__(self, other): 
        return other and self.quantity == other.quantity and self.price == other.price
    def __lt__(self, other): 
        return other and self.price < other.price
    
    
  


        

    




