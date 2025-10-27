# num=int(input("Enter a number: "))
#
# a=num
# d=0
# while num>0:
#     r=num%10
#     d=(d*10)+r
#     num=num//10
# if a==d:
#     print("paliandrome")
# else:
#     print("not palinadrome")

# def is_armstrong(num):
#     digits =str(num)
#     power=len(digits)
#     total=sum(int(digit)** power for digit in digits)
#
#     return total==num
#
# num=int(input("enter a number"))
# if is_armstrong(num):
#     print("yes")
# else:
#     print("no")

    def fact_check(num):
        if num==1:
            return 1
        else:
            return num*fact_check(num-1);
    num=int(input("Enter a number:"))
    print(fact_check(num))