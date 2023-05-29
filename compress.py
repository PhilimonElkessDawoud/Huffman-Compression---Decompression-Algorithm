from fileParser import Parser
from priorityQ import heap
from BinaryTree import BinaryTree
from Huffman import HuffmanCode

class Compressor:

    def __init__(self, path) -> None:
        self.path = path
        self.file = Parser(self.path)
        self.heap = heap()
        self.tree = BinaryTree()
        self.huffman = HuffmanCode()

    def compress(self):

        self.file.parseOriginal()

        self.heap.build(self.file.frequencies)

        self.tree.buildBinaryTree(self.heap.queue)

        self.huffman.generateCode(self.heap.queue)

        encodedtext = self.huffman.encode(self.file.text)

        self.file.write(encodedtext)

        print("File Compressed Successfully!")


    def decompress(self):
        self.file.parseCompressed()
        decodedtext = self.huffman.decode(self.file.encodedText)
        print(decodedtext)
        print("File Decompressed Successfully!")