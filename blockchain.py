blockchain=[]
i=0
def block(blockchain):
    return blockchain[-1]
def add(last_transaction=block(blockchain)):
    global i
    i=i+1
    blockchain.append([last_transaction,i])
    print(blockchain)
add()
add()

    