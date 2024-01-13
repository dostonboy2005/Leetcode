a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
for i in range(a,1000):
    if i%b==0:
        print(i)
        break