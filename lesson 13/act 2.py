def fac(n):
    if(n==1 or n==2):
        return 1
    return n*fac(n-1)
n = int(input("Enter a number:"))
print("Factorial of",n,"is: ",fac(n))
