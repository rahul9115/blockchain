genesis_block={'previous_hash':'',
               'transaction':[] 

}

i=0
blockchain=[genesis_block]
open_transactions=[]
sender="Rahul"
def open_transaction(receiver,amount,sender=sender):
    transaction={'sender': sender,'receiver':receiver,'amount': amount}
    open_transactions.append(transaction)

def get_transaction_value():
    print("Enter the recipient")
    receiver=input()
    print("Enter the transaction amount")
    transaction_amount=input()
    return receiver,transaction_amount

def mine_block(blockchain):
    hashed=' '
    last_block=blockchain[-1]
    print(last_block)
    global i
    i=i+1
    for key in last_block:
        if i==1:
            value=last_block[key]
            hashed=hashed+str(value)
        else:
            for i in key:
                print("This is i",i)
                
                value=key.get(i)
                print(value)
                hashed=hashed+str(value)
    block={'previous_hash':hashed,
           'transaction':open_transactions 
    }
    blockchain.append([block])
    print(blockchain)
while True:
    print("Enter 1 to add transaction")
    print("Enter 2 to mine block")
    value=input()
    if value=='1':
        data=get_transaction_value()
        receiver,amount=data
        open_transaction(receiver,amount=amount)
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
    if value=='2':
        mine_block(blockchain)
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
    else:
        continue        

