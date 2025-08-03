largenum=int(input("Enter a number:"))
a=largenum
smallnum=int(input("Enter a smaller number:"))
b=smallnum
lcm=0
while(smallnum):
    numstore=smallnum
    smallnum=largenum%smallnum
    largenum=numstore

print("HCF is:",largenum )

lcm=(a*b)/largenum
print("LCM is:",lcm)