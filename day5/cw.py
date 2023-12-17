def hash(func):
    def wrapper():
        print("#"*10)
        func()
        print("#"*10)
    return wrapper
def star(func):
    def wrapper():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper


""" @hash
@star """


def world():
    print("World")
        
hash(star(world))()