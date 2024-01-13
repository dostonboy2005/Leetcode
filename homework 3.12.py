lst=[int(input())for i in range(3)]
lst=sorted(lst)
a=0
for i in range(2):
    a+=lst[i]**2
b=lst[-1]
if a==b*b:
    print(True)
else:
    print(False)        