import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit="0123456789"
symbol="()[]{};:'#$%&*@"
all=lower+upper+digit+symbol
length=10
password="".join(random.sample(all,length))
print("the generated password is:",password)
