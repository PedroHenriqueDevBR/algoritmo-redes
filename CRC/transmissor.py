def main():
    msize = int(input('Digite o tamanho da mensagem: '))
    mess = []
    print('Digite a mensagem: ')
    for i in range(msize):
        mess.append(int(input('Digite o {}º bit: '.format(i+1))))

    dsize = int(input('Digite o tamanho do divisor: '))
    div = []
    for i in range(dsize):
        div.append(int(input('Digite o {}º bit: '.format(i+1))))

    print()
    print('A mensagem digitada foi: ', end='')
    for i in range(msize):
        print(mess[i], end='')
    print()

    print('O divisor digitado foi: ', end='')
    for i in range(dsize):
        print(div[i], end='')
    print()

    for i in range(dsize):
        mess.append(0)

    msize = (msize + dsize) - 1

    print()
    print('A nova mensagem é: ', end='')
    for i in range(msize):
        print(mess[i], end='')
    print()

    res = []
    rsize = msize
    for i in range(msize):
        res.append(mess[i])

    n = 0
    for i in range(dsize):
        res[i] = mess[i]^div[i] # XOR
        n = i

    m = 0
    flag = 0
    count = 0
    k = 0
    rem = [0] * (dsize)
    while n <= msize:
        while flag == 0:
            if res[m] == 0:
                m += 1
            else:
                flag = 1
        flag = 0

        for i in range(m, dsize + m):
            if res[i] == 0 or res[i] == 1:
                count += 1
        
        print()
        print('count: ', count)
        
        if count == dsize:
            for i in range(m, dsize + m):
                res[i] = res[i]^div[k]
                k += 1
            k = 0
        else:
            break
        count = 0
        n = (dsize + m) + 1
        print()
        for i in range(msize):
            print(res[i], end='')
        print()

    rsize = msize - 1

    for i in range(1, dsize):
        mess[rsize] = res[rsize]
        rsize -= 1

    print()
    print('CRC gerado: ', end='')
    for i in range(msize):
        print(mess[i], end='')
    print()

    rsize = msize - 1

    for i in range(dsize - 1, 0, -1):
        rem[i] = res[rsize]
        rsize -= 1

    print()
    print('Resto: ', end='')
    for i in range(1, dsize):
        print(rem[i], end='')
    print()


if __name__ == "__main__":
    main()
