user_info=[ {
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

def register():
    username=input("Enter your username")
    password=input("Enter your password")
    if username in user_info:
        print("Username already exists, choose another username")
        username=input("Enter your username")
    user_info[username] = password
    print("Thank you for registering")

 
def login():
    username=input("Enter the username")
    password=input("Enter the password")

    if username not in user_info and password not in user_info:
        print("Username or password is incorrect")
    else:
        print("Login successgful!!!")

while True:
    print("1. Register")
    print("2. login")
    print("3. logout")
    
    choice=int(input("Enter your choice (1-3)"))

    if choice==1:
        register()
    elif choice==2:
        login()
    elif choice==3:
        print("Logging out")
        exit()