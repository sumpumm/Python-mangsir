class Person:
    def __init__(self,name,age,password):
        self.name=name
        self._age=age
        self.__password=password
    
    
    @property # getter ko lagi
    def password(self):
        return self.__password  
      
    @password.setter # setter ko lagi
    def password(self,password):
        self.__password=password
    
    
person=Person('ram',12,'pass123')
print(person.name)
print(person._age)
#print(person.__password) we can't access this directly because it is private
person.password='sumpum123'
print(person.password)