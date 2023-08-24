array=[1,2,3,4,5,6,5,4,5,3,2,1]
dict1={}
for i in array:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print(dict1)
print("max:")
large=0
for i in dict1:
    if(dict1[i]>large):
        large=dict1[i]
for i in dict1:
    if large==dict1[i]:
        print(i)
# code for printing minimum frequency key
print("min:")
minimum=None
for i in dict1:
    if minimum==None:
        minimum=dict1[i]
    if minimum>dict1[i]:
        minimum=dict1[i]
for i in dict1:
    if minimum==dict1[i] :
        print(i)
