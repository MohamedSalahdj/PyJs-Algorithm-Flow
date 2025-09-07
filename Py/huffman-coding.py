import heapq

class HeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

    def __repr__(self):
        return f'Node(data: {self.data}, freq: {self.freq})'


class Huffman:
    def __init__(self, message):
        freqHash = {}

        # Calculate frequency of each character in the message
        for char in message:
            if char in freqHash:
                freqHash[char] += 1
            else:
                freqHash[char] = 1
        
        # Create a heap node for each character and add it to minHeap
        self.minHeap = []
        for char, freq in freqHash.items():
            newNode = HeapNode(char, freq)
            heapq.heappush(self.minHeap, newNode)

        print(self.minHeap)



def main():
    message = 'internet'
    huffman = Huffman(message)

main()