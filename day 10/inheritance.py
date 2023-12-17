#types of inheritance
#multiple
#multilevel
#simple
#Hybrid

class GrandFather:
    house="luxury"
    
    def get_house(self):
        return self.house
    
class Father(GrandFather):
    car="Mercedes"
    house="banglow"
    
    def get_house(self):
        print(super().get_house())
        return self.house


class GrandMother:
    jewellery="goldieeeee"
        

class Son(Father):
    console="PS5"



grandFather=GrandFather()    
father=Father()
print(father.get_house())

