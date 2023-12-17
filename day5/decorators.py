#only cude to decorate the code


def star(func):
    def wrapper():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper

@star
def hello():
    print("Hello Sumpumm")
    
hello()

