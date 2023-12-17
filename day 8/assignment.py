import os
file_name=input("enter file name : ")
def create(): 
    try: 
        open(file_name,"x")
    except Exception as e:
        print("error file exists")
    
def write():
    global file_name   
    with open(file_name,"a") as f:
        content=input("Enter contents to write in file : ")
        f.write("\n",content)
 

def delete():
    delete=input("Enter the file you want to delete : ")
    os.remove(delete)
    

print("""1.Create file
2.append to file
3.delete file
      """)
ch=int(input("Enter your choice : "))
if ch ==1:
    create()
elif ch==2:
    write()
elif ch==3:
    delete()
else:
    exit()
    

    