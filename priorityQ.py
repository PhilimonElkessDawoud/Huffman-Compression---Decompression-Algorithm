import heapq
from BinaryTree import Node

class heap:
    
    def __init__(self) -> None:
        self.queue = []

    def build(self, frequencies: dict):
        for key in frequencies:
            frequency = frequencies[key]
            node = Node(key,frequency)
            heapq.heappush(self.queue , node)