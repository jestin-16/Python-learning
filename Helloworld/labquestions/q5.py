list1 = []
list2 = []

n1 = int(input("Enter number of elements in first list: "))
for i in range(n1):
    list1.append(int(input("Enter element: ")))

n2 = int(input("Enter number of elements in second list: "))
for i in range(n2):
    list2.append(int(input("Enter element: ")))

if len(list1) == len(list2):
    print("Lists are of equal length")
else:
    print("Lists are of different length")

# b) Check equal sum
if sum(list1) == sum(list2):
    print("Sum of both lists is equal")
else:
    print("Sum of both lists is not equal")


common_elements = []

for x in list1:
    if x in list2 and x not in common_elements:
        common_elements.append(x)

if common_elements:
    print("Common elements present:", common_elements)
else:
    print("No common elements in both lists")
