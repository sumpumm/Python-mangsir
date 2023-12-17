lists=[{'Username':'JijashShrestha','Password':'1234'},
      {'Username':'Sammpumm','Password':'0123'},
      {'Username':'Suyashh','Password':'suyash123'}]

def registration():
    username=input('USERNAME : ')
    password=input('PASSWORD : ')
    lists.append({'Username':username,'Password':password})


def login():
    username=input('USERNAME : ')
    password=input('PASSWORD : ')
    
    for i in lists:
        if i['Username']==username and i['Password']==password:
            print('Login Successful !!')
            
        else:
            print('Invalid username or password. Please try again.')
        break
def user():
        
            print(' Hello ! Welcome To The Back...!!!')
            print('''1. Enter 1 for registration
2. Enter 2 for login 
3. Enter 3 for logout
4. Enter 4 for exit 
            ''')
            
            choice=int(input('Please enter your choice as shown above : '))
            if choice>4:
                 print('invalid input !! please choose your choice between 1 - 4')
                 exit
            elif choice==1:
                    print('Please enter following details for your registration. Thank you !!')
                    registration()
                    print('Thank you for registration !!''\n')
                    print('1. Enter 1 for login')
                    print('2. Enter 2 for returning to homepage')
                    print('3. Enter 3 to exit')
                    reg_choice=int(input('Enter your choice from 1 - 3: '))
                    if reg_choice==1:
                         login()
                    elif reg_choice==2:
                         user()
                    elif reg_choice==3:
                       print('Thank you !!')
                       exit
                            
                    
            elif choice==2:
                print('Please enter your Login username and password')
                login()
            elif choice==3:
                    print('Are you sure you want to logout ?')
                    logout_choice=input('Click Y if yes otherwise N :')
                    if logout_choice=='y':
                        print('thank you !')
                        
                    if logout_choice=='n':
                        
                        user()
            elif choice==4:
                    print('Thank you !!')
            
      
user()