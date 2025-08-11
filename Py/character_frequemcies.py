class CharFrequency:
    def asci(self, messgae):
        freq = [0] * 127
        for letter in messgae:
            code = ord(letter)
            freq[code] +=1

        for i in range(len(freq)):
            if freq[i] > 0:
                print(f"{chr(i)} --> {freq[i]}")


def main():
    obj = CharFrequency()
    message = "hello world"
    obj.asci(message)

main()