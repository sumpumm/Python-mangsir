from abc import ABC,abstractmethod

class Computer:
    def run(self,app):
        self.process(app)
        
    @abstractmethod
    def process(self,app):
        pass

class Mobile(Computer):
    def process(self,app):
        print("Mobie is running ",app)

class Laptop(Computer):
    def process(self,app):
        print("laptop is running ",app)
         
    
apple=Mobile()
apple.run("messenger")
acer=Laptop()
acer.run("viber")
