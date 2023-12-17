#used in cases where we dont know the number of arguments to be passed
#arguments are taken in tupples
def sum(*args):
    total=0
    for i in args:
        total+=i
    print(total)

sum(1,2,2,5)
    
#homework
#create a function that takes name and print their name