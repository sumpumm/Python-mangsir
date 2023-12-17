users=[ {
        'user_name':'sumpumm',
        'password':'123456'
    },{
        'user_name':'aastha',
        'password':'smp123'
    },{
        'user_name':'sadil123',
        'password':'helloWorld'
    }
]

for i in users:
    print(i['user_name'])
    
users.append({'user_name':'jiyash','password':'uwuuu'})

def logIn():
    print("Welcome to login portal")
    user_name=input("Username : ")
    password=input("password : ")   
    for i in users:
        if i['user_name']==user_name and i['password']==password :
            
            print("You are logged in!")
            break