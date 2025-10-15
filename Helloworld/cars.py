guess_count=0
guess_limit=3
command=""
while command.lower() != "quit":
    guess_count+=1
    guess=input('>')
    if guess=='start':
        print('Car started...Ready to go')
    elif guess=='stop':
        print('Car stopped')
    elif guess=='quit':
        break
    else:
        print(f"i don't understand that")

else:
    print("you failed")