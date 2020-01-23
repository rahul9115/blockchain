import hashlib
import json
import pickle
from collections import OrderedDict
genesis_block={'previous_hash': '','transaction':[],'proof':100}
blockchain=[genesis_block]
open_transactions=[]
participants=[]
global Mining_reward
Mining_reward=0
sender="Rahul"
global value4
value4=False
value5=False
global balance
balance=0
def load_data():
   with open("blockchain.p",mode='rb') as f:
        file_content=pickle.loads(f.read())
        print(file_content)
        global blockchain
        global open_transactions
        #blockchain=json.loads(file_content[0][:-1])
        #open_transactions=json.loads(file_content[1])
        blockchain=file_content['chain']
        open_transactions=file_content['ot']
        
        
        """updated_blockchain=[]
        for block in blockchain:
            updated_block={
                'previous_hash':block['previous_hash'],
                'transaction':[OrderedDict([('sender',tx.get('sender')),('receiver',tx.get('receiver')),('amount',tx.get('amount'))]) for tx in block['transaction'] if tx.get('sender') is not None],
                'proof':block['proof']


            }
            updated_blockchain.append(updated_block)
        blockchain=updated_blockchain"""    

load_data()        
def save_data():
    with open("blockchain.p",mode='wb') as f:
        save_data={
            'chain':blockchain,
            'ot':open_transactions
        }
        f.write(pickle.dumps(save_data))
    
def verify_transaction(sender,amount):
    global balance
    balance=balance_miner(sender)
    if balance>=int(amount):
        return True
    else:
        return False    

def open_transaction(receiver,amount,sender=sender):
    if verify_transaction(sender,amount):
        #transaction={'sender': sender,'receiver':receiver,'amount': amount}
        transaction=OrderedDict([('sender',sender),('receiver',receiver),('amount',amount)])
        open_transactions.append(transaction)
        participant={sender,receiver}
        participants.append(participant)
    else:
        print("Transaction Failed")
        return False    

def get_transaction_value():
    print("Enter the recipient")
    receiver=input()
    print("Enter the transaction amount")
    transaction_amount=input()
    return receiver,transaction_amount
def valid_proof(transaction,hashed,proof):
    guess=(str(transaction)+str(hashed)+str(proof)).encode()
    new_hash=hashlib.sha256(guess).hexdigest()
    print(new_hash)
    return new_hash[0:2]=='00'
def check():
    last_block=blockchain[-1]
    proof=0
    while not valid_proof(last_block['transaction'],last_block['previous_hash'],proof):
        proof=proof+1
    return proof    

def mine_block(blockchain):
    global Mining_reward
    hashed=' '
    print(blockchain)
    last_block=blockchain[-1]
    Mining_reward+=10
    reward={
        'reward':'Mining',
        'receiver':sender,
        'amount':Mining_reward
    }
    open_transactions.append(reward)
    hashed=hashlib.sha256(json.dumps(last_block).encode()).hexdigest()
    #hashed='-'.join([str(last_block[key]) for key in last_block])
    proof=check()
    print(proof)
    block={'previous_hash':hashed,
           'transaction':open_transactions,
           'proof': proof
    }

    blockchain.append(block)
    print(blockchain)
    save_data()
    return True
def check_balance(participant):
    global balance
    tx_sender=[[tx['amount'] for tx in block['transaction'] if tx.get('sender')==participant and tx.get('reward')!='Mining']for block in blockchain]
    amount_sent=0
    amount_received=0
    print(tx_sender)
    for tx in tx_sender:
        if len(tx)>0:
            for i in tx:
                amount_sent+=int(i)
    balance=balance_miner(participant)
    print(balance)
    balance=balance-amount_sent            
    tx_receiver=[[tx['amount'] for tx in block['transaction'] if tx.get('receiver')==participant and tx.get('reward')!='Mining']for block in blockchain]
    for tx in tx_receiver:
        if len(tx_receiver)>0:
            for i in tx:
               amount_received+=int(i)
    balance=balance+amount_received           
    return balance
def balance_miner(participant):
    tx_receiver=[[tx['amount'] for tx in block['transaction'] if tx.get('receiver')==participant]for block in blockchain]
    amount_received=0
    for tx in tx_receiver:
        if len(tx_receiver)>0:
            for i in tx:
               amount_received+=int(i)
    return amount_received
    
def verify_blockchain(blockchain):
    n=len(blockchain)-1
    i=0
    global value1
    while n>=0:
        for block in blockchain:
            if i==n:
                for key in block:
                    if key=='previous_hash':
                        value=block.get(key)
                        print(blockchain[n-1])
                        hashed=hashlib.sha256(json.dumps(blockchain[n-1]).encode()).hexdigest()
                        print("this is value",value)
                        print("this is hash",hashed)
                        if value==hashed and valid_proof(blockchain[n-1]['transaction'][:-1],blockchain[n-1]['previous_hash'],block['proof'])==True:
                            value1=True
                        else:
                            value1=False
                            break
            
            i=i+1
        n=n-1
    if value1==True:
        return True
    else:
        return False    
                      
while True:
    print("Enter 1 to add transaction")
    print("Enter 2 to mine block")
    print("Enter 3 to Verify the blockchain")
    print("Enter 4 for Participants")
    print("Enter 5 to check balances")
    print("Enter 6 to quit")
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
    elif value=='2':
        if mine_block(blockchain):
            open_transactions=[]
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
    elif value=='3':
        value2=verify_blockchain(blockchain)
        if value2==True:
            print("Valid blockchain")
        else:
            print("Invalid blockchain")
    elif value=='4':
        print(participants)

    elif value=='5':
        while True:
            participant=input("enter the participant")
            print(blockchain)
            value5=False
            value4=False
            miner=[]
            miner=[[tx['receiver']for tx in block['transaction'] if tx.get('reward')=='Mining']for block in blockchain]
            print(miner)
            for i in participants:
                for j in i:
                    if j==participant:
                        value4=True
                        break        
            for i in miner:
                for j in i:
                    print(j)
                    if j==participant:
                        print("I am in")
                        value5=True
                        break
            print(value4," ",value5)                
            if value4==True:
                balance=check_balance(participant)
                print("balance",balance)
                    
            if value5==True:
                reward=balance_miner(participant)
                print("balance =",reward)
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
                print("enter the valid participant")
                continue           
    elif value=='6':
        break           
    else:
        continue        
        
