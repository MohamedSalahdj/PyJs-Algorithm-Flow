class CharFrequency:
    def asci(self, messgae):
        freq = [0] * 127
        for letter in messgae:
            code = ord(letter)
            freq[code] +=1

        for i in range(len(freq)):
            if freq[i] > 0:
                print(f"{chr(i)} --> {freq[i]}")

    def frequency_dict(self, message):
        freq = {}
        for i in message:
            freq[i] = freq.get(i, 0) + 1
        
        for key, value in freq.items():
            print(f"{key} -- > {value}")
        
        self.sort_dict(freq)

    def sort_dict(self, freq):
        freq_array = [[0 for _ in range(2)] for _ in range(len(freq))]
        i = 0

        # Convert the Hashtable(dictionary) into a 2D integer array
        for key, value in freq.items():
            freq_array[i][0] = ord(key)
            freq_array[i][1] = value
            i +=1
        
        # Sort the array in descending order based on the frequency count
        self.sort(freq_array, 0, len(freq_array) - 1)

        print("Print Sorted data ...")
        for ascii_code, count in freq_array:
            print(f"{chr(ascii_code)} --> {count}") 

    def sort(self, array, start, end):
        if end <= start:
            return
        
        midpoint = (start + end) // 2
        self.sort(array, start, midpoint)
        self.sort(array, midpoint+1, end)

        self.merge(array, start, midpoint, end)
        
    def merge(self, array, start, midpoint, end):

        # Calculate lengths of two sub-arrays
        left_length = midpoint - start +1
        right_length = end - midpoint

        # Create temporary sub-arrays
        left_array = [[0, 0] for _ in range(left_length)]
        right_array = [[0, 0] for _ in range(right_length)] 

        # Copy data to temporary sub-arrays
        for i in range(left_length):
            left_array[i][0] = array[start + i][0]
            left_array[i][1] = array[start + i][1]

        for j in range(right_length):
            right_array[j][0] = array[midpoint + 1 + j][0]
            right_array[j][1] = array[midpoint + 1 + j][1]
        i = j = 0
        k = start
        
        # Merge the temporary sub-arrays back into the original array
        while i < len(left_array) and j < len(right_array):
            if left_array[i][1] <= right_array[j][1]:
                array[k][0] = left_array[i][0]
                array[k][1] = left_array[i][1]
                i +=1 
            else:
                array[k][0] = right_array[j][0]
                array[k][1] = right_array[j][1]
                j +=1 
            k +=1
        
        # Move remaining items from left_half, if any
        while i < len(left_array):
            array[k][0] = left_array[i][0]
            array[k][1] = left_array[i][1]
            i +=1
            k +=1
        
        # Move remaining items from right_half, if any
        while j < len(right_array):
            array[k][0] = right_array[j][0]
            array[k][1] = right_array[j][1]
            j +=1
            k +=1


def main():
    obj = CharFrequency()
    message = "hello world"
    # obj.asci(message)
    print("-"*45)
    obj.frequency_dict(message)
    

main()