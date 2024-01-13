a=int(input("Enter the number: "))
b=int(input("Enter second number: "))
c=input("Enter the time E.X: \"second\" \"minute\" \"hour\": ")
if c=="second":
    print("Damage ",(a*b)," in second")
if c=="minute":
    print("Damage ",(a*b)*60," in minute")
if c=="hour":
    print("Damage ",(a*b)*3600," in hour")        