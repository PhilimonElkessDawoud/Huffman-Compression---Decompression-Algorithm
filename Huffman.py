import heapq
from binAsci import binasci

class HuffmanCode:
    

    def __init__(self) -> None:
        self.codes = {}
        self.huffmanTree = None 


    def __generateCodeHelper(self, root, code: str):
        if root is None:
            return
        
        if root.data is not None:
            self.codes[root.data] = code
            return
        
        self.__generateCodeHelper(root.left, code + '0')
        self.__generateCodeHelper(root.right, code + '1')


    def generateCode(self, queue: list):
        self.huffmanTree = heapq.heappop(queue)
        duplicatePointer = self.huffmanTree
        self.__generateCodeHelper(duplicatePointer, '')


    def encode(self, text):

        encoded = ""
        binary = ""

        for char in text:
            binary += self.codes[char]


        if (len(binary) % 8) != 0:
            remaining = 8 - (len(binary) % 8)
            for i in range(remaining):
                binary += "0"

        encoded = binasci.toString(binary)
        
        return encoded 
    

    def decode(self, text):

        decoded = ""
        binary = binasci.toBinary(text)
        root = self.huffmanTree

        for bit in binary:

            if root.data is not None:
                decoded += root.data
                root = self.huffmanTree

                if bit == "0":
                    root = root.left

                elif bit == "1":
                    root = root.right

            elif bit == "0":
                root = root.left

            elif bit == "1":
                root = root.right
                  
        return decoded 
