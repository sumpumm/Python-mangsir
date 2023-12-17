#function without a name
#use to create smaller and reusable functions

""" s=lambda a:a+10
print(s(10))
 """
 
def mul(n):
     return lambda x:x*n
 
doubler=mul(2)
print(doubler(2))


trippler=mul(3)
print(trippler(2)) 