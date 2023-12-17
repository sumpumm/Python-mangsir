def sub(a,b):
    return a-b

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        
    
def exp(a,b):
    return a**b

def mod(a,b):
    return a%b


while True :
    a=int(input("Enter a number : "))
    b=int(input("ENter a number : "))
    
    print("""
        ..............MENU..............
         1. +
         2. -
         3. *
         4. /
         5. %
         6. **
         7.exit
      """)
    choice=int(input("Enter your choice : "))


    if(choice==1):
        print(add(a,b))
    elif(choice==2):
        print(sub(a,b))
    elif(choice==3):
        print(mul(a,b))
    elif(choice==4):
        print(div(a,b))
    elif(choice==5):
        print(mod(a,b))
    elif(choice==6):
        print(exp(a,b))
    else:
        break


    


