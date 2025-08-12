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
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] = freq[i] + 1
        
        for key, value in freq.items():
            print(f"{key} -- > {value}")


def main():
    obj = CharFrequency()
    message = "hello world"
    obj.asci(message)
    print("-"*45)
    obj.test(message)

main()