# from fileParser import Parser
# from priorityQ import heap
# from BinaryTree import BinaryTree
# from Huffman import HuffmanCode


# file1 = Parser(path)
# file1.parseOriginal()

# print(file1.byteNum)
# print(file1.frequencies)

# heap1 = heap()
# heap1.build(file1.frequencies)

#print(heap1.queue)

# tree1 = BinaryTree()
# tree1.buildBinaryTree(heap1.queue)

#print(heap1.queue)

# huffman1 = HuffmanCode()
# huffman1.generateCode(heap1.queue)

# print(huffman1.codes)

# encodedtext = huffman1.encode(file1.text)

# print(text)

# file1.write(encodedtext, huffman1.codes)

# file1.parseCompressed()

#print(file1.encodedText)

# decodedtext = huffman1.decode(file1.encodedText)

# print(decodedtext)