def maxelement(a):
    length=len(a)
    if length==1:
        return a[0]
    return max(a[0],maxelement (a[1:]))
a=[1,2,42,567,53,325,689,6]
print("Largest number of the array is",maxelement(a))

