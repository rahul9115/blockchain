blockchain=[[100]]
value=0
block=[]
def transaction():
    global block
    value=int(input("Enter the transaction value"))
    block.append(blockchain[-1])
    block.append(value)
    blockchain.append(block)
    print(blockchain)
    block=[]
while True:
    print("enter 1 to add transaction")
    print("enter 2 to validate the blockchain")
    value1=int(input("Enter the value"))
    if value1==1:
        transaction()
        while True:
            print("do you want to continue y/n")
            value2=input("Enter the value")
            if value2=='y':
                value3=True
                break
            elif value2=='n':
                value3=False
                break
            else:
                print("Enter either y/n")
                continue
        if value3==True:
            continue
        else:
            break
    if value1==2:
        n=len(blockchain)-1
        k=0
        i=0
        print(n)
        value4=False
        while n>0:
            for blocks in blockchain:
                
                if i==n:
                  
                    if blocks[0]==blockchain[n-1]:
                        value4=True
                    else:
                        value4=False    
                else:
                    i=i+1
                    continue
            n=n-1
            i=0
        if value4==True:
            print("Valid Blockchain")
        else:
            print("Invalid ")              
                                
    else:
        continue
            
