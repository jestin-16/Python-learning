num=int(input("Enter a number: "))
r=num
while num>0:
    digit=num%10
    d=d+(digit*digit*digit)
    num=num//10

if d==r:
    print("armstrong")
else:
    print("not armstrong")