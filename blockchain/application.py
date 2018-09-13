################################################################################
#   application.py
#
#   Initialization of the App
#
#   13.09.2018  Created by:  zhenya
################################################################################
from block import *
from chain import *

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Chain()
local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
local_blockchain.blocks[2].transactions = fake_transactions
local_blockchain.validate_chain()


#class Application:
#  def __init__(self):
#    self.game = Game()
#    self.root = Tk()
#    self.gui  = GameGUI(self.root, self.game)
