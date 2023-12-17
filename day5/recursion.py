#using recursion recreate range function


def ran(a):
    if a==0:
        return 0
    else:
        return ran(a-1)
    
a=int(input("Enter a number:"))
