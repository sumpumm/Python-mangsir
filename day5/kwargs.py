#similar to args but the parameters are stored in dictionary and we have to give the index in the parameter
def person(**details):
    print(details['name'])
    
person(name='ram',age=12)