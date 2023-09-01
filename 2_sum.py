arr=eval(input("enter array:"))
sum1=int(input("enter sum:"))
i=0
j=len(arr)-1
while(i<j):
    if((arr[i]+arr[j])==sum1):
        print(i,j)
        j=j-1
        i=i+1
    elif((arr[i]+arr[j])>sum1):
        j=j-1
    else:
        i=i+1
    
