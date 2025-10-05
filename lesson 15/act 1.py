def checksort(a):
    length=len(a)
    if length==1 or length==0:
        return True
    return a[0]<= a[1] and checksort(a[1:])
a=[1,2,3,5,6,8,2]
if checksort(a):
    print("Yes it is sorted")
else:
    print("No it is not sorted")
    