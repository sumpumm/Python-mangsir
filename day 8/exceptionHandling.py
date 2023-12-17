def divider():
    num1=int(input("Enter a number : "))
    num2=int(input("Enter a number : "))
    if num2==5:
        raise Exception("5 is not accepted")
    else: 
        print(num1/num2)



while True:
    try:
        divider()
    except Exception as e:
        print(e)
        
