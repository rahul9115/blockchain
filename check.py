a=[1,1,1,4,4,4,4]
count=0
max1=0
for i in range(0,len(a),1):
    for j in range(0,len(a),1):
        if(i!=j and a[i]==a[j]):
            count=count+1
   
    if count>max1:
        max1=count
    count=1    

           
print(max1)            