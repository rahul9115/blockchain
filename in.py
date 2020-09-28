a=[100,180,260,310,40,535,40,0,0,800]
sum1=0
min1=a[0]
k=False
for i in range(1,len(a),1):
    
    k=False
    
    if(a[i-1]<a[i] or a[i-1]==a[i]):
        
        ub=a[i]
        s=min(a[i-1],a[i])
        min1=min(s,min1)
    else:
        print("This",ub,min1)
        sum1=sum1+(ub-min1) 
        min1=a[i]  
        ub=0
        
        k=True
if k==False:
    sum1=sum1+(ub-min1)

print(sum1)        
    
