class Hamming {

    def __init__(self, palavra, paridade):
        self.word = word
        self.parity = parity
        self.checkers = []
        self.word_distributed = []
        self.verify_positions = dict()
        self.calculated_position = dict()

    # todo: implement calculate parity
    def parity_calculated(self, verificador):
        positions_bit = [] #bits_das_posicoes = []
        count = 0

        for i in range(len(self.word_distributed)):
            if self.word_distributed[i] is None:
                continue
            positions_bit = i + 1
            if positions_bit in verify_positions:
                bits_das_posicoes.append(palavra_distribuida[i])

        for bit in bits_das_posicoes:
            if bit == 1:
                contador += 1

        if paridade == '0':  # 0 = paridade par
            if contador % 2 == 0:  # Deu par
                return 0
            else:
                return 1
        else:  # então paridade é impar
            if contador % 2 == 0:
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
            if case <= numero:
                result.append(verify)
                sum_number += verify

        self.calculated_position[number] = result


    def number_has_verify(self, verify):
        positions = []
        for bit in self.word_distributed:
            if verify in self.calculated_position[bit]:
                positions.append(bit)
        return positions


    def word_distributed(self):
        i = 0
        word_position = 0
        while word_position < len(self.word):
            position = i + 1
            if self.is_verify(position):
                self.word_distributed.append(None)
                self.checkers.append(posicao)
            else:
                self.word_distributed.append(int(palavra[posicao_na_palavra]))
                word_position += 1
            i += 1


    def is_verify(self, number):
        while numero >= 1 and numero % 2 == 0:
            numero /= 2
        return numero == 1

}