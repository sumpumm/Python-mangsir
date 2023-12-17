class house:
   # color="red"
    #doors=1
    #windows=2
    
    def __init__(self,window,color,door,price):
        self.price=price
        self.window=window
        self.color=color
        self.door=door
        
    def get_colour(self):
        return self.color 
    
    def __eq__(self,value):
        return self.window==value.window        
    def __gt__(self,other):
        return self.price>other.price
    



sumpumm=house(window=5,color="black",door=2,price=100000)
aastha=house(7,"grey",5,20000000)
#print(sumpumm.color)
""" print(sumpumm.set_color("buruuuuu"))
print(sumpumm.get_colour()) """
print(sumpumm.__eq__(aastha))
print(sumpumm.__gt__(aastha))


#string method
