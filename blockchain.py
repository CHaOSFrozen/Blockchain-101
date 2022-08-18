# Module 1 - Create a Blockchain

# Datetime returns the extact date the block is mined 
import datetime
# Hash the blocks
import hashlib
# Encode the blocks before hasing them
import json
# Create and object of flask class, web application itself
# Jsonify returns the messages in postman when we interact with our blockchain
from flask import Flask, jsonify

# Part 1 - Building a Blockchain

class Blockchain: 
    # Takes one same argument which refer to the object we create
    def __init__(self):
        # Chain containg the blocks, List containing the blocks
        self.chain = []
        # Creates the Genesis Block (First Block of the Blockchain)
        # Each Block will have it's own proof
        # Second Argument is a key that each block will have (previous hash value)
        # But since its the firs, gensis block, it will not have any previous hash value.
        # Arbitrary value 
        self.create_block(proof = 1, previous_hash = '0')
    # Create a new block with all the features in a blockchain and will append this new mined block to the blockchain
    def create_block(self, proof, previous_hash):
        # Make a dictionary that will define each block in the blockchain with its four essential keys, index of the block, time stamp, proof of the block, previous hash 
        block = {'index' : len(self.chain) + 1 ,
                 'timestamp' : str(datetime.datetime.now()) ,
                 'proof' : proof,
                 'previous_hash' : previous_hash}
        # Append the block to the chain 
        self.chain.append(block)
        # Display the information of this block in Postman
        return block
    # Gets the previous block
    def get_previous_block (self):
        # Returns the last index of the chain
        return self.chain[-1]
    # First Argument, self (apply this proof of work method from instance object that would be created)
    # Second Argument, previous proof, in order to make the problem that miners have to solve, the previous proof has to be there
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False 
        # Introudce while loop to increment this new proof to check if its the right proof 
        while check_proof is False:
            # Leading Zeros ID (define the problem) (more = harder)
            # EASY CHALLENGE (CAN MAKE IT HARDER)
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof +=1
        return new_proof
                
            
            
            
      


# Part 2 - Mining our Blockchain