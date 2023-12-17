def sub(a,b):
    return a-b

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    try:
       if b==0:
           raise Exception("Divide by 0 not possible!")
       else:
           return a/b
    except Exception as e:
        print(e)
    
def exp(a,b):
    return a**b

def mod(a,b):
    if a>b:
        return a
    else:
        return a%b