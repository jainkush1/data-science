def checkifsame(num1,num2):
    if ((num1^num2)!=0):
        print("They are not same")
    else:
        print("They are same")
    
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))

checkifsame(num1,num2)
