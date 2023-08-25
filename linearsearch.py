def linearsearch(arr,target):
    for i in arr:
        if(arr[i]==target):
            return i
    return -1
arr=eval(input())
target=int(input())
print(linearsearch(arr,target))
