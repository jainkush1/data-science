def subArraysum(arr, n, sum):
    for i in range(n):
        curr_sum=arr[i]
        j=i+1
        while j <= n:
            if curr_sum==sum:
                print ("Sum found between")
                print("indexes %d and %d"%(1, j-i))
                return 1
            if curr_sum > sum or j==n:
                break

            curr_sum=curr_sum + arr[j]
            j+=1
    print("No sun array found")
    return 0
arr=[23,6,2,2,56,1,0,9]
n=len(arr)
sum=10
subArraysum(arr,n,sum)