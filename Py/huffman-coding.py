import heapq

class HeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq