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
        return f'Node(data: {self.data}, freq: {self.freq}, left: {self.left}, right: {self.right})'


class Huffman:
    def __init__(self, message):
        self.internal_char = chr(0)
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
            heapq.heappush(self.minHeap, (newNode.freq, newNode))

        # Debug: Print the initial minHeap
        print(self.minHeap)

        # Construct Huffman tree by repeatedly extracting nodes from min heap
        while len(self.minHeap) > 1:
            left_freq, left_node = heapq.heappop(self.minHeap)
            right_freq, right_node = heapq.heappop(self.minHeap)
            newFreq = left_freq + right_freq
            top = HeapNode(self.internal_char, newFreq)
            top.left = left_node
            top.right = right_node
            heapq.heappush(self.minHeap, (top.freq, top))

        # Debug: Print the final minHeap (should contain only the root of the Huffman tree)
        print('-'*45)
        print(self.minHeap)


def main():
    message = 'internet'
    huffman = Huffman(message)

main()