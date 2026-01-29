row=[]
col=[]
for i in range(10):
    row.append(i)
for i in range(10):
    col.append(i)
for i in row:
    for j in col:
        print(row[i],row[j],end=" ")
    print()