num=int(input("Enter a number: "))
r=num
d=0
while num>0:
    digit=num%10
    d=d*10+digit
    num=num//10

if d==r:
    print("palinandrome")
else:
    print("not palindrome")