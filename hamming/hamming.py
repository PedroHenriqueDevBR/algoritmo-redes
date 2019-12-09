class Hamming:

    def __init__(self, word, parity):
        self.word = word
        self.parity = parity
        self.checkers = []
        self.word_distributed = []
        self.verify_positions = dict()
        self.calculated_position = dict()
        self.error_counter = 0
        self.error_position = 0
        self.verifiers_received = []
    

    def data_validation(self):
        if len(self.word) == 0:
            return False
        for bit in self.word:
            if bit != '0' and bit != '1':
                return False
        if self.parity != 'odd' and self.parity != 'even':
            return False

        return True


    def word_generate(self):
        if self.data_validation():
            self.word_distributer() # 1001 = |V|V|1|V|0|0|1|
            self.aply_hamming()
            return True
        return False


    def check_word(self):
        if self.data_validation():
            for bit in self.word:
                self.word_distributed.append(int(bit))

            self.make_checkers_null() # 1011001 = |V|V|1|V|0|0|1|
            self.aply_hamming()
            self.compare_checkers()
            return True
        return False

    
    def aply_hamming(self):
        for i in range(len(self.word_distributed)):
            bit = self.word_distributed[i]
            if bit is not None:
                self.calculate_verity(i + 1) # EX: '11' = 8 + 2 + 1

        for verify in self.checkers:
            self.verify_positions[verify] = self.number_has_verify(verify) # EX: '1' = 3, 5, 7, 11, 13

        for i in range(len(self.word_distributed)):
            bit = self.word_distributed[i]
            if bit is None:
                position = i + 1
                response = self.parity_calculated(position) # bit 1 = 0, bit 2 = 1, bit 4 = 0, bit 8 = 1
                self.word_distributed[i] = response

    
    def make_checkers_null(self):
        for i in range(len(self.word_distributed)):
            position = i + 1
            if self.is_verify(position):
                self.verifiers_received.append(int(self.word[i]))
                self.checkers.append(position)
                self.word_distributed[i] = None


    def compare_checkers(self):
        aux_checkers = []

        for i in range(len(self.word_distributed)):
            position = i + 1
            if position in self.checkers:
                aux_checkers.append(self.word_distributed[i])

        for i in range(len(aux_checkers)):
            if aux_checkers[i] != self.verifiers_received[i]:
                self.error_counter += 1
                self.error_position += pow(2, i)


    def parity_calculated(self, verify):
        positions_bits = []
        positions_of_verify = self.verify_positions[verify]
        count = 0

        for i in range(len(self.word_distributed)):
            if self.word_distributed[i] is None:
                continue
            positions = i + 1
            if positions in positions_of_verify:
                positions_bits.append(self.word_distributed[i])

        for bit in positions_bits:
            if bit == 1:
                count += 1

        if self.parity == 'even':
            if count % 2 == 0:
                return 0
            else:
                return 1
        elif self.parity == 'odd':
            if count % 2 == 0:
                return 1
            else:
                return 0


    def calculate_verity(self, number):
        aux_checkers = []
        result = []
        sum_number = 0

        for verify in self.checkers:
            if verify < number:
                aux_checkers.append(verify)
        aux_checkers.sort(reverse=True)

        for verify in aux_checkers:
            case = sum_number + verify
            if case <= number:
                result.append(verify)
                sum_number += verify

        self.calculated_position[number] = result


    def number_has_verify(self, verify):
        positions = []
        for bit in self.calculated_position:
            if verify in self.calculated_position[bit]:
                positions.append(bit)
        return positions


    def word_distributer(self):
        i = 0
        word_position = 0
        while word_position < len(self.word):
            position = i + 1
            if self.is_verify(position):
                self.word_distributed.append(None)
                self.checkers.append(position)
            else:
                self.word_distributed.append(int(self.word[word_position]))
                word_position += 1
            i += 1


    def is_verify(self, number):
        while number >= 1 and number % 2 == 0:
            number /= 2
        return number == 1

def main():
    word = '0'
    parity = 'even'

    hamming = Hamming(word, parity)

    if hamming.check_word():
        print('os dados estão válidos')
        print('Palavra distribuida')
        print(hamming.word_distributed)
        print('Verificadores')
        print(hamming.checkers)
        print('Total de erros')
        print(hamming.error_counter)
        print('Posição do erro')
        print(hamming.error_position)
    else:
        print('dados inválidos')

if __name__ == '__main__':
    main()
