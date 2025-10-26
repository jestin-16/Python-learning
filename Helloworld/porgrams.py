num=int(input("Enter a number: "))

a=num
d=0
while num>0:
    r=num%10
    d=(d*10)+r
    num=num//10
if a==d:
    print("paliandrome")
else:
    print("not palinadrome")