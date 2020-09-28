a=[1,2,3,-1,4]
sum1,m=a[0],a[0]
for i in range(1,len(a)):
    sum1=max(sum1+i,i)
    m=max(sum1,m)
print(m)    