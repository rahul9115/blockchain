blockchain=[]
blockchain1=[]
global value2
value2=False
global i
i=1
global i1
i1=0
global i2
i2=0
def get_last_transaction(blockchain):
    return blockchain[-1]
def block(transaction_amount,last_transaction=[1]):
    blockchain.append([last_transaction,transaction_amount])
    print(blockchain)
def block1(transaction_amount):
    blockchain.append(transaction_amount)
    print(blockchain)
def validate(blockchain):
    
    n=len(blockchain)-1
    i=0
    value=False
    while n>=0:
        for block in blockchain:
            
            i=i+1
            if i==(n+1):
                if block[0]==blockchain[n-1]:
                    value=True
                else:
                    print("Invalid blockchain")
                    value=False
                    break
        if value==False:
            break        
        n=n-1 
    if value==True:
        return True
    else:
        return False                   
while True:
    print("Enter 1:To enter new transaction")
    print("Enter 2:To add transaction")
    print("Enter 3:To validate the blockchain")
    value=int(input("Enter the value "))
    
    if value==1:
        transaction_amount=int(input("Enter new transaction amount"))
        i1=i1+1
        while True:
            value1=input("Do you want to continue [y/n]")
            if value1=='n' or value1=='y':
                break
            else:
                print("please enter valid input")
                continue
        if value1=='y':
            continue
        else:
            break



    elif value==2:
        if i1>i2:
            if i==1:
                block1([transaction_amount])
                i=i+1
                i2=i2+1
            else:
                block(transaction_amount,get_last_transaction(blockchain))
                i2=i2+1
            while True:
                value1=input("Do you want to continue [y/n]: ")
                if value1=='n' or value1=='y':
                    break
                else:
                    print("please enter valid input")
                    continue
            if value1=='y':
                continue
            else:
                break
        else:
            print("Please Enter a new transaction")
            continue    
   
    elif value==3:
        print(blockchain)
        blockchain1=blockchain
        blockchain[0]=[200]
        value2=validate(blockchain)
        if value2==True:
            print("Valid BlockChain")
            print(blockchain)
        else:
            print("invalid Blockchain")
            blockchain=blockchain1
            print(blockchain)


        continue





    else:
        print("please enter valid input")
        continue    
