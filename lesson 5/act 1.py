number=int(input("Enter a number:"))

og_num=number
rev_num=0

while number>0:
    digit = number%10
    rev_num= rev_num*10 + digit
    number//=10

if og_num==rev_num:
    print(og_num,"is palindrome")
else:
    print(og_num,"is not a palindrome")
