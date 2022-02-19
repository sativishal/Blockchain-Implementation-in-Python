import hashlib


def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class Blockchain:

    def __init__(self):
        hashLast = hashGenerator('The hash of the last Block')
        hashStart = hashGenerator('The hash of the current Block')
        genesis = Block('The First Block of the Blockchain',
                        hashStart, hashLast)
        self.chain = [genesis]

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data+prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)


bc = Blockchain()
bc.add_block('I am the Second Block')
bc.add_block('I am the third Block')
bc.add_block('I am the fourth Block')
bc.add_block('I am the fifth Block')
bc.add_block('I am the Sixth Block')

for blocks in bc.chain:
    print("The list of the Blocks Information", blocks.__dict__)
