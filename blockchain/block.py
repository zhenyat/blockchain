################################################################################
#   block.py
#
#   Model: Block (class Block)

#   11.09.2018  Created by: zhenya
################################################################################
import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp     = datetime.datetime.now()
    self.transactions  = transactions
    self.previous_hash = previous_hash
    self.nonce         = nonce
    self.hash          = self.generate_hash()
    
  # Prints block contents
  def print_block(self):   
    print("timestamp:    ", self.timestamp)
    print("transactions: ", self.transactions)
    print("current hash: ", self.generate_hash())
 
  # Generates hash of the blocks contents
  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
    block_hash     = sha256(block_contents.encode())
    
    return(block_hash.hexdigest())