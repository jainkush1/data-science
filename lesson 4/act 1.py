number=int(input("Enter a number:"))
digits=len(str(number))
resultnumber=0
temp=number
while temp>0:
    digit=temp%10
    resultnumber += digit ** digits
    temp//=10

if number == resultnumber:
    print(number,"is an amstrong number")
else:
    print(number,"is not an amstrong number")
    
