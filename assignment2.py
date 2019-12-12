names=[]
for i in range(0,5,1):
    a=input("Enter names: ")
    names.append(a)
for i in names:
    print(len(i))
for i in names:
    if len(i)>5:
        print("Names with length greater than 5 : "+i)
for i in names:
    for j in i:
        if j=='n' or j=='N':
            print("Names containing 'n' or 'N'"+i)
            break
#Pop names out of the list
n=len(names)-1
while n>=0:
    print(names.pop())
    n=n-1               

    