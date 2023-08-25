def search(nums: [int], target: int):
    s=0
    e=len(nums)-1
    mid=s+e//2
    while(s<=e):
        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            s=mid+1
            mid=(s+e)//2
        else:
            e=mid-1
            mid=(s+e)//2
    return -1
arr=[1,3,4,5,6,8]
target=6
a=search(arr,target)
print(a)
