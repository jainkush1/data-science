largenum=int(input("Enter a number:"))
smallnum=int(input("Enter a smaller number:"))

while(smallnum):
    numstore=smallnum
    smallnum=largenum%smallnum
    largenum=numstore

print("HCF is:",largenum )
