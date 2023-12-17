""" #function le suru ma local check garcha ani balla global check garcha

a=10 #global variable

def number():
    a=11       #local variable
    print(a)

number()
print(a) """
""" 
a=10

def number():
    global a
    a=11       #over ride huney bhayo kina ki function bhitra global vanera point out gareko cha
    print(a)
    
number()
print(a)
 """
a=10
def outer():
    a=11
    def inner():
        print("inner sees a as",a)
    inner()
    print("outer sees a as ",a)
    
outer()
print("main sees a as ",a)




