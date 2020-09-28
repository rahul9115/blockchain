block_list=[]
a=True
a1=True
while True:
    a=int(input("Enter the required input : \n 1:Enter a new number \n 2: Check the blockchain \n 3: Display the blockchain 4: Exit"))
    m=[]
    
    if a==1:
        
        b=int(input("Enter the number"))
        if not len(block_list):
            while True:
                m.append(b)
                y=input("Do you want to continue ? y/n")
                if y=='y':
                    b=int(input("Enter the number"))
                    continue
                else: 
                    break    
        else:
            m.append(block_list[-1])
            while True:
                m.append(b)
                y=input("Do you want to continue ? y/n")
                if y=='y':
                    b=int(input("Enter the number"))
                    continue
                else: 
                    break    
        
        block_list.append(m)
           
    if a==2:
       for i in range(len(block_list)-1,-1,-1):
           print(block_list[i][0],block_list[i-1])
           if block_list[i][0]!=block_list[i-1]:
               a1=False
               break
       if a1==True:
           print("Perfect Blockchain")
       else:
           print("Error in blockchain")           


    if a==3:
        print(block_list)
    if a==4:
        break    
                
