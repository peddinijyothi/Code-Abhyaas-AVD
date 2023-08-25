def l_num(arr):
    s=0
    e=len(arr)-1
    while(s<e):
        mid=s+(e-s)//2
        if((mid%2==0 and arr[mid]==arr[mid+1]) or (mid%2==1 and arr[mid]==arr[mid-1])):
           s=mid+1
        else:
            e=mid
    return arr[s]
arr=eval(input())
print(l_num(arr))
