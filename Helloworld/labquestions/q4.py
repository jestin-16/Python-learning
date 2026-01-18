# names=[]
# n=int(input("Enter the number of names: "))
# for i in range(n):
#     names.append(input(f"Enter name {i+1}: "))
# count=0
# for name in names:
#     count+=name.lower().count("a")
#
# print("List of names:", names)
# print("Total occurrences of letter 'a':", count)

names=[]
n=int(input("enter no of names:"))
for i in range(n):
    names.append(input("enter name:"))
count=0
for name in names:
    count+=name.lower().count('a')

print(count)