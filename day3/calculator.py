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
    print(a+b)
elif(choice==2):
    print(a-b)
elif(choice==3):
    print(a*b)
elif(choice==4):
    if(b==0):
        print("Error!, divide by zero not possible")
    else:    
        print(a/b)
elif(choice==5):
    print(a%b)
elif(choice==6):
    print(a**b)
else:
    print("Goodbye")
    exit

