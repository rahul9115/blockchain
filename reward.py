"""It seems that tx['reward']=='Mining' and tx.get('reward')=='Mining' are different 
since both of them do different functions. If i use tx['reward'] then it throws an error. Since in every block 
it will look for tx['reward'] but if in case i use tx.get['reward'] then it will only take those dictionaries
which have the following specified"""
blockchain=[{'previous_hash': '', 'transaction': []}, {'previous_hash': '-[]', 'transaction': [{'reward': 'Mining', 'receiver': 'Rahul', 'amount': 10}]}, {'previous_hash': "-[]-[{'reward': 'Mining', 'receiver': 'Rahul', 'amount': 10}]", 'transaction': [{'sender': 'Rahul', 'receiver': 'rahul', 'amount': '2'}, {'reward': 'Mining', 'receiver': 'Rahul', 'amount': 20}]}]
miner=[]
for block in blockchain:
    for tx in block['transaction']:
        print(tx)
        if tx.get('reward')=='Mining':
            miner.append(tx['receiver'])
print(miner)