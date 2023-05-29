import heapq

class Node:
    def __init__(self, data, freq) -> None:
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq 

class BinaryTree:

    def __init__(self) -> None:
        pass

    def buildBinaryTree(self, queue: list):
        while len(queue) > 1:

            node1 = heapq.heappop(queue) 
            node2 = heapq.heappop(queue) 

            freqSum = node1.freq + node2.freq
            newnode = Node(None, freqSum)

            newnode.left = node1
            newnode.right = node2

            heapq.heappush(queue, newnode)