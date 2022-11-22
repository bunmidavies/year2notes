def binarySearch(l, r, nums, target):
    if (l >= r):
        if (nums[l] == target):
            return l
        else:
            return -1
    midpoint = (l + ((r - l) // 3))
    print(midpoint)
    print(nums[l:r+1])
    print("l = " + str(l) + " r = " + str(r))
    if (nums[midpoint] > target):
        return binarySearch(l, midpoint - 1, nums, target)
    elif (nums[midpoint] < target):
        return binarySearch(midpoint + 1, r, nums, target)
    else:
        return midpoint

num = [4,8,9,10,12,13,19]
print(binarySearch(0,len(num)- 1,num,13))
