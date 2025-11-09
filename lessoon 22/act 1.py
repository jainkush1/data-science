def getMaxLength(a, a_size):
    counter=0
    maxones = 0

    for i in range(0,a_size):
        if (a[i]==1):    
                counter += 1
                maxones = max(maxones,counter)
        else:
            counter = 0
    return maxones

a = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 11]
a_size=len(a)

print("Max 1's: ",getMaxLength(a,a_size))       