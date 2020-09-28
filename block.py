from time import time
class Block:
    def __init__(self,previous_hash,transactions,proof,time=time()):
        self.previous_hash=previous_hash
        self.transactions=transactions
        self.timestamp=time
        self.proof=proof