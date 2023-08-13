a=[4,6,2,8,5,4,5,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)