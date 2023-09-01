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
