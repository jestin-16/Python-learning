# i=1
# while i<=5:
#     print(i)
#     i=i+1
# sum=0
# for i in range(10):
#     sum=sum+i
# print(sum)

# i=1
# while i<=5:
#     print("*" * i)
#     i=i+1

# num=9
# i=0
# while i<3:
#     n=int(input("Guess: "))
#     i=i+1
#     if n==num:
#         print("Correct!")
#         break
#     else:
#         print("Incorrect!")
# else:
#     print("your chances over")

secret_number = 9
guess_count=0
guess_limit =3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count=guess_count+1
    if guess==secret_number:
        print('You won!')
        break

else:
    print('You lose :(')