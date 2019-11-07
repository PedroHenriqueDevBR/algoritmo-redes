def main():
    # palavra = '1000111001'
    palavra_distribuida = []
    verificadores = []
    palavra_calculada = dict()
    posicoes_do_verificador = dict()
    palavra = input('Digite a palavra: ')
    paridade = input('Digite a paridade: [0] Par ou [1] Impar: ')

    distribui_palavra(palavra, palavra_distribuida, verificadores)

    for i in range(len(palavra_distribuida)):
        letra = palavra_distribuida[i]
        if letra is not None:
            calcula_verificador(i+1, verificadores, palavra_calculada)


    for verificador in verificadores:
        posicoes_do_verificador[verificador] = verificar_se_numero_faz_parte_do_verificador(verificador, palavra_calculada)

    
    for i in range(len(palavra_distribuida)):
        letra = palavra_distribuida[i]
        if letra is None:
            posicao_do_verificador = i + 1
            retorno = calcula_paridade(posicao_do_verificador, posicoes_do_verificador[posicao_do_verificador], palavra_distribuida, paridade)
            palavra_distribuida[i] = retorno


    for i in range(len(palavra_distribuida)):
        print('| {} |'.format(i+1), end='')
    print()
    for i in range(len(palavra_distribuida)):
        print('| {} |'.format(palavra_distribuida[i]), end='')
    print()



def calcula_paridade(verificador, posicoes_que_ele_aparece, palavra_distribuida, paridade):
    bits_das_posicoes = []
    contador = 0


    for i in range(len(palavra_distribuida)):
        if palavra_distribuida[i] is None:
            continue
        posicao_do_loop = i+1
        if posicao_do_loop in posicoes_que_ele_aparece:
            bits_das_posicoes.append(palavra_distribuida[i])


    for bit in bits_das_posicoes:
        if bit == 1:
            contador += 1


    if paridade == 0: # 0 = paridade par
        if contador % 2 == 0: # Deu par
            return 0
        else:
            return 1
    else: # então paridade é impar
        if contador % 2 == 0:
            return 1
        else:
            return 0


def verificar_se_numero_faz_parte_do_verificador(verificador, palavra_calculada):
    # import pdb; pdb.set_trace()
    posicoes = []
    for palavra in palavra_calculada:
        if verificador in palavra_calculada[palavra]:
            posicoes.append(palavra)
    # print('{} == {}'.format(verificador, posicoes))
    return posicoes


def calcula_verificador(numero, verificadores, palavra_calculada):
    aux_verificadores = []
    resultado = []
    soma = 0
    
    for verificador in  verificadores:
        if verificador < numero:
            aux_verificadores.append(verificador)
    aux_verificadores.sort(reverse=True)

    for verificador in aux_verificadores:
        condicao = soma + verificador
        if condicao <= numero:
            resultado.append(verificador)
            soma += verificador
    palavra_calculada[numero] = resultado


def mostra_(dicionario):
    for item in dicionario:
        print('{} == {}'.format(item, dicionario[item]))


def distribui_palavra(palavra, palavra_distribuida, verificadores):
    i = 0
    posicao_na_palavra = 0
    while posicao_na_palavra < len(palavra):
        posicao = i + 1
        if eh_verificador(i+1):
            palavra_distribuida.append(None)
            verificadores.append(posicao)
        else:
            palavra_distribuida.append(int(palavra[posicao_na_palavra]))
            posicao_na_palavra += 1
        i += 1


def eh_verificador(numero):
    while numero >= 1 and numero % 2 == 0:
        numero /= 2
    return numero == 1


if __name__ == '__main__':
    main()
