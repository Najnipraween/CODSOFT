a=int(input("enter the first number= "))
b=int(input("enter the second number="))
n=int(input("enter the number 1 to 4="))
if n==1:
   print("sum=",a+b)
elif n==2:
    print("sub=",a-b)
elif n==3:
    print("mul=",a*b)
elif n==4:
    print("div=",a/b)
else:
    print("invalid")
