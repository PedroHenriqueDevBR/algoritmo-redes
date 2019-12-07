class Hamming:

    def __init__(self, word, parity):
        self.word = word
        self.parity = parity
        self.checkers = []
        self.word_distributed = []
        self.verify_positions = dict()
        self.calculated_position = dict()

    def word_generate(self):
        self.word_distributer()

        for i in range(len(self.word_distributed)):
            bit = self.word_distributed[i]
            if bit is not None:
                self.calculate_verity(i + 1)

        for verify in self.checkers:
            self.verify_positions[verify] = self.number_has_verify(verify)

        # Todo: Falta só isso
        for i in range(len(self.word_distributed)):
            bit = self.word_distributed[i]
            if bit is None:
                position = i + 1
                response = self.parity_calculated(self.checkers[position])
                self.word_distributed[i] = response


    def parity_calculated(self, verify):
        positions_bits = [] #bits_das_posicoes = []
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
            if count % 2 == 0:  # Deu par
                return 0
            else:
                return 1
        elif self.parity == 'odd':
            if count % 2 == 0:
                return 1
            else:
                return 0


    def calculate_verity(self, number):
        aux_checkers = [] # aux_verificadores
        result = [] # resultado
        sum_number = 0 # soma

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




'''
 Tesntando a classe Hamming, não faça isso em casa, seja organizado
'''

def main():
    # Palavra exemplo
    # palavra = '1000111001'

    word = '1000111001'
    parity = 'odd'

    hamming = Hamming(word, parity)
    hamming.word_generate()


if __name__ == '__main__':
    main()
