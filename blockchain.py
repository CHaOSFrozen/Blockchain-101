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

# Create a web application 
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
# Create a Blockchain
blockchain = Blockchain()

# USE route() decorator to tell Flask what URL should trigger our function
# Mining a new Block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': "Congratulations, you just mined a block!",
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash']}
    return jsonify(response), 200 


# Check if the blockchain is valid    
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': "Blockchain is Valid" }
    else:
        response = {'message' : "Blockchain is not Valid" }
    return jsonify(response), 200 
        

# Getting the Full Blockchain 
@app.route('/get_chain', methods=['GET'])
# Display Chain
def get_chain():
    response = {'chain' : blockchain.chain,
                'length' : len(blockchain.chain)}
    return jsonify(response), 200 

# Running the Application
app.run(host = '0.0.0.0', port = 5000)
    
