class CRC_receptor:
    def __init__(self):
        self.remainder = []
        self.crc_message = []
        self.generator = []
        self.rest = []
        
        self.remainder_size = 0
        self.generator_size = 0
        self.message_size = 0


    def getData(self):
        wrong = False

        while True:
            message = input("Enter the CRC message (Ex. 11001): ")
            if len(message) == 0:
                wrong = True
            else:
                for i in range(len(message)):
                    if message[i] not in ['0', '1']:
                        wrong = True
            if not wrong:
                self.message_size = len(message)
                for i in range(self.message_size):
                    self.crc_message.append(int(message[i]))
                break
            else:
                print("Message is wrong!")
                wrong = False

        while True:
            gen = input("Enter the generator (Ex. 1011): ")
            if len(gen) == 0:
                wrong = True
            else:
                if gen[0] != '1' or gen[-1] != '1':
                    wrong = True
                for i in range(len(gen)):
                    if gen[i] not in ['0', '1']:
                        wrong = True
            if not wrong:
                self.generator_size = len(gen)
                for i in range(self.generator_size):
                    self.generator.append(int(gen[i]))
                break
            else:
                print("Generator is wrong!")
                wrong = False


    def showData(self):
        print("\nEntered CRC message: ", end='')
        for i in range(self.message_size):
            print(self.crc_message[i], end='')
        print()

        print("Entered generator: ", end='')
        for i in range(self.generator_size):
            print(self.generator[i], end='')
        print()


    def convert(self):
        bits_to_right = 0
        lenght = 0
        count = 0
        error = False
        j = 0

        self.remainder_size = self.message_size
        for i in range(self.message_size):
            self.rest.append(self.crc_message[i])

        for i in range(self.generator_size):
            self.rest[i] = self.crc_message[i]^self.generator[i]
            lenght = i

        while lenght <= self.message_size:
            while True:
                if self.rest[bits_to_right] == 0:
                    bits_to_right += 1
                    if bits_to_right >= len(self.rest):
                        break
                else:
                    break

            if bits_to_right >= len(self.rest):
                break
            else:
                for i in range(bits_to_right, self.generator_size + bits_to_right):
                    if self.rest[i] == 0 or self.rest[i] == 1:
                        count += 1

                print("\nCount: ", count)
                if count == self.generator_size:
                    for i in range(bits_to_right, self.generator_size + bits_to_right):
                        self.rest[i] = self.rest[i]^self.generator[j]
                        j += 1
                    j = 0
                else:
                    break

                count = 0
                lenght = (self.generator_size + bits_to_right) + 1

                for i in range(self.message_size):
                    print(self.rest[i], end='')
            
        self.remainder_size = self.message_size - 1

        self.remainder = [-1] * (self.generator_size - 1)

        for i in range(len(self.remainder) - 1, - 1, - 1):
            self.remainder[i] = self.rest[self.remainder_size]
            self.remainder_size -= 1
        
        print("\n\nRemainder is: ", end='')
        for i in range(self.generator_size - 1):
            print(self.remainder[i], end='')
            if self.remainder[i] == 1:
                error = True

        if error == False:
            print("\nNo error is present in the received message")
        else:
            print("\nError is present in the received message")


def main():
    receptor = CRC_receptor()
    receptor.getData()
    receptor.showData()
    receptor.convert()

if __name__ == "__main__":
    main()
