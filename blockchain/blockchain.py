#!/usr/bin/env python3
################################################################################
#   blockchain.py
#
#   App main module (script)
#
#   13.09.2018  Created by: zhenya
################################################################################

from chain import Chain

block_one_transactions   = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions   = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions        = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Chain()
local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
local_blockchain.blocks[2].transactions = fake_transactions
local_blockchain.validate_chain()
