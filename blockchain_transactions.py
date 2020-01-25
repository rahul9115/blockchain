import hashlib
import json
genesis_block={'previous_hash':'_','open_transactions':[]}
blockchain=[genesis_block]
open_transactions=[]
block={}
global balance
balance=0
amount=0
sr=[]
proof=0
def transactions(recipient, amount=amount,sender="Rahul"):
    transaction={'sender':sender,'recipient':recipient,'amount':amount}
    open_transactions.append(transaction)
def hash(blockchain):
    block=blockchain
    hashed=hashlib.sha256(json.dumps(block).encode()).hexdigest()
    return hashed
def valid_proof(previous_hash,transaction,proof):
    guess=(str(transaction)+str(previous_hash)+str(proof)).encode()
    pow=hashlib.sha256(guess).hexdigest()
    return pow[:2]=='00'
def check():
    proof=0
    while not valid_proof(blockchain[-1].get('previous_hash'),blockchain[-1].get('open_transactions'),proof):
        proof=proof+1
    return proof             
def sender():
    sender=[]
    block=blockchain[-1]
    block1=block.get('open_transactions')
    sender=[{'sender':i.get('sender'),'receiver':i.get('recipient')}for i in block1[:-1]]
    sr.append(sender)
    print(sr)
while True:
    print("1: Add transactions")
    print("2:Mine a block")
    print("3: Validate the chain")
    print("4: check the senders and recipients")
    print("5:Sender balance and recipient balance")
    print("6: Exit")
    value=input('Enter the value')
    if value=='1':
        amount=0
        recipient=input("Enter the Recipient")
        amount=int(input("Enter the amount"))
        if amount<=balance:
            transactions(recipient=recipient,amount=amount)
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
        else:
            print('Sorry you dont have enough money ')
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
    elif value=='2':
        hashed=' '
        hashed=hash(blockchain[-1])
        print(hashed)
        balance=balance+10
        mining_reward={'reward':balance, 'To':"Rahul"}
        open_transactions.append(mining_reward)    
        proof=check()
        block={'previous_hash':hashed,
        'open_transactions':open_transactions,
        'proof':proof
        }
        blockchain.append(block)
        print(blockchain)
        open_transactions=[]
    elif value=='3':
        n=len(blockchain)-1
        i=0
        while n>0:
            for blocks in blockchain:
                if i==n:
                    hash_check=blocks.get('previous_hash')
                    hashed=hash(blockchain[n-1])
                    
                   
                    if hashed==hash_check and valid_proof(blockchain[n-1].get('previous_hash'),blockchain[n-1].get('open_transactions'),blocks.get('proof'))==True:
                        value4=True
                    else:
                        value4=False
                i=i+1        
            n=n-1
            i=0
        if value4==True:
            print("Valid Blockchain")
        else:
            print("Invlaid Blockchain")
    elif value=='4':
        sender()        
    elif value=='6':
        break
    else:
        continue                            


        