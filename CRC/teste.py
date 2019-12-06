class CRC:
    def __init__(self, tamanho):
        self.mess = [-1] * tamanho
        self.div = [-1] * tamanho
        self.res = [-1] * tamanho
        self.rem = [-1] * tamanho
        self.rmes = [-1] * tamanho
        self.rdiv = [-1] * tamanho
        self.rres = [-1] * tamanho
        self.rrem = [-1] * tamanho
        
        self.msize = 0
        self.dsize = 0
        self.rsize = 0
        self.rmsize = 0
        self.rdsize = 0
        self.rrsize = 0

    def obterDados(self):
        self.msize = int(input("\nDigite o tamanho da palavra: "))
        palavra = input("Digite a palavra (Ex. 11001): ")
        for i in range(self.msize):
            self.mess[i] = int(palavra[i])

        self.dsize = int(input("\nDigite o tamanho do divisor: "))
        divisor = input("Digite o divisor (Ex. 10110): ")
        for i in range(self.dsize):
            self.div[i] = int(divisor[i])

    def mostrarDados(self):
        print("\nA palavra digitada foi: ", end='')
        for i in range(self.msize):
            print(self.mess[i], end='')
        print()

        print("O divisor digitado foi: ", end='')
        for i in range(self.dsize):
            print(self.div[i], end='')
        print()

    def converter(self):
        n = 0
        m = 0
        flag = 0
        k = 0
        count = 0

        for i in range(self.msize, self.msize + self.dsize):
            self.mess[i] = 0

        self.msize = (self.msize + self.dsize) - 1

        print("\nNova palavra: ", end='')
        for i in range(self.msize):
            print(self.mess[i], end='')
        
        self.rsize = self.msize
        for i in range(self.msize):
            self.res[i] = self.mess[i]

        for i in range(self.dsize):
            self.res[i] = self.mess[i]^self.div[i]
            n = i

        while n <= self.msize:
            while flag == 0:
                if self.res[m] == 0:
                    m += 1
                else:
                    flag = 1
            flag = 0

            for i in range(m, self.dsize + m):
                if self.res[i] == 0 or self.res[i] == 1:
                    count += 1

            print("\nCount: ", count)
            if count == self.dsize:
                for i in range(m, self.dsize + m):
                    self.res[i] = self.res[i]^self.div[k]
                    k += 1
                k = 0
            else:
                break

            count = 0
            n = (self.dsize + m) + 1

            for i in range(self.msize):
                print(self.res[i], end='')
            
            self.rsize = self.msize - 1

            for i in range(1, self.dsize):
                self.mess[self.rsize] = self.res[self.rsize]
                self.rsize -= 1

            print("\nO código CRC gerado foi: ", end='')
            for i in range(self.msize):
                print(self.mess[i], end='')
            
            self.rsize = self.msize - 1

            for i in range(self.dsize - 1, 0, -1):
                self.rem[i] = self.res[self.rsize]
                self.rsize -= 1
            
            print("\nO resto foi: ", end='')
            for i in range(1, self.dsize):
                print(self.rem[i], end='')


def main():
    crc = CRC(20)
    crc.obterDados()
    crc.mostrarDados()
    crc.converter()

if __name__ == "__main__":
    main()
