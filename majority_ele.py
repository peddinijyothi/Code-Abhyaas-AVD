arr=eval(input("enter list:"))
count=0
ele=0
for i in arr:
    if(count==0):
        ele=i
        count=1
    elif(ele==i):
        count=count+1
    else:
        count=count-1
print(ele)

# for n/3 elements

arr=eval(input("enter array:"))
n=len(arr)/3
d={}
for i in arr:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
for i in d:
    if(d[i]>=n):
        print(i)

