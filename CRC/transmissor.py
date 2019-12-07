class CRC:
    def __init__(self, tamanho):
        self.frame_check_sequence = [-1] * tamanho
        self.final_message = [-1] * tamanho
        self.generator = [-1] * tamanho
        self.rest = [-1] * tamanho
        
        self.remainder_size = 0
        self.generator_size = 0
        self.message_size = 0

    def getData(self):
        wrong = False

        while True:
            message = input("Enter the message (Ex. 11001): ")
            for i in range(len(message)):
                if message[i] not in ['0', '1']:
                    wrong = True
            if not wrong:
                self.message_size = len(message)
                for i in range(self.message_size):
                    self.final_message[i] = int(message[i])
                break
            else:
                print("Message is wrong!")
                wrong = False

        while True:
            gen = input("Enter the generator (Ex. 1011): ")
            if gen[0] != '1' or gen[-1] != '1':
                wrong = True
            for i in range(len(gen)):
                if gen[i] not in ['0', '1']:
                    wrong = True
            if not wrong:
                self.generator_size = len(gen)
                for i in range(self.generator_size):
                    self.generator[i] = int(gen[i])
                break
            else:
                print("Generator is wrong!")
                wrong = False

    def showData(self):
        print("\nEntered message: ", end='')
        for i in range(self.message_size):
            print(self.final_message[i], end='')
        print()

        print("Entered generator: ", end='')
        for i in range(self.generator_size):
            print(self.generator[i], end='')
        print()

    def convert(self):
        bits_to_right = 0
        lenght = 0
        count = 0
        j = 0

        for i in range(self.message_size, self.message_size + self.generator_size):
            self.final_message[i] = 0

        self.message_size = (self.message_size + self.generator_size) - 1

        print("\nNew message: ", end='')
        for i in range(self.message_size):
            print(self.final_message[i], end='')
        
        self.remainder_size = self.message_size
        for i in range(self.message_size):
            self.rest[i] = self.final_message[i]

        for i in range(self.generator_size):
            self.rest[i] = self.final_message[i]^self.generator[i]
            lenght = i

        while lenght <= self.message_size:
            while True:
                if self.rest[bits_to_right] == 0:
                    bits_to_right += 1
                else:
                    break

            for i in range(bits_to_right, self.generator_size + bits_to_right):
                if self.rest[i] != -1:
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

        for i in range(1, self.generator_size):
            self.final_message[self.remainder_size] = self.rest[self.remainder_size]
            self.remainder_size -= 1

        print("\nCRC generated: ", end='')
        for i in range(self.message_size):
            print(self.final_message[i], end='')
        
        self.remainder_size = self.message_size - 1

        for i in range(self.generator_size - 1, 0, -1):
            self.frame_check_sequence[i] = self.rest[self.remainder_size]
            self.remainder_size -= 1
        
        print("\nframe check sequence: ", end='')
        for i in range(1, self.generator_size):
            print(self.frame_check_sequence[i], end='')
        print()


def main():
    crc = CRC(50)
    crc.getData()
    crc.showData()
    crc.convert()

if __name__ == "__main__":
    main()
