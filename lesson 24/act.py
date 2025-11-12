def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        right = total-left-x
        if left == right:
            return i
        left+=x
    return -1
arr=[-4,6,2,0,0,1,1]
print("Elements:",pivotIndex(arr))

