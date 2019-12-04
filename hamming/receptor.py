def main():
    verificadores = []
    verificadores_recebidos = []
    palavra_calculada = dict()
    posicoes_do_verificador = dict()

    palavra_distribuida = []
    palavra = '01100001111011'
    paridade = '1'

    for bit in palavra:
        palavra_distribuida.append(int(bit))

    tornar_verificadores_none(palavra_distribuida, verificadores, verificadores_recebidos)

    for i in range(len(palavra_distribuida)):
        letra = palavra_distribuida[i]
        if letra is not None:
            calcula_verificador(i + 1, verificadores, palavra_calculada)

    for verificador in verificadores:
        posicoes_do_verificador[verificador] = verificar_se_numero_faz_parte_do_verificador(verificador,
                                                                                            palavra_calculada)

    for i in range(len(palavra_distribuida)):
        letra = palavra_distribuida[i]
        if letra is None:
            posicao_do_verificador = i + 1
            retorno = calcula_paridade(posicoes_do_verificador[posicao_do_verificador],
                                       palavra_distribuida, paridade)
            palavra_distribuida[i] = retorno

    mostra_resultado(palavra_distribuida, verificadores_recebidos, verificadores)


def tornar_verificadores_none(palavra, verificadores, verificadores_recebidos):
    for i in range(len(palavra)):
        posicao = i + 1
        if eh_verificador(posicao):
            verificadores_recebidos.append(palavra[i])
            verificadores.append(posicao)
            palavra[i] = None


def mostra_resultado(palavra_distribuida, verificadores_recebidos, verificadores_encontrados):
    erros = 0
    posicao_do_erro = 0
    aux_verificadores = []

    for i in range(len(palavra_distribuida)):
        posicao = i + 1
        if posicao in verificadores_encontrados:
            aux_verificadores.append(palavra_distribuida[i])

    for i in range(len(aux_verificadores)):
        if aux_verificadores[i] != verificadores_recebidos[i]:
            erros += 1
            posicao_do_erro += pow(2, i)

    if erros > 0:
        print('Palavra incorreta')
        print('Erro lozalizado na posicao {}'.format(posicao_do_erro))
    else:
        print('Palavra correta')


def calcula_paridade(posicoes_que_ele_aparece, palavra_distribuida, paridade):
    bits_das_posicoes = []
    contador = 0

    for i in range(len(palavra_distribuida)):
        if palavra_distribuida[i] is None:
            continue
        posicao_do_loop = i + 1
        if posicao_do_loop in posicoes_que_ele_aparece:
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


def verificar_se_numero_faz_parte_do_verificador(verificador, palavra_calculada):
    posicoes = []
    for palavra in palavra_calculada:
        if verificador in palavra_calculada[palavra]:
            posicoes.append(palavra)
    return posicoes


def calcula_verificador(numero, verificadores, palavra_calculada):
    aux_verificadores = []
    resultado = []
    soma = 0

    for verificador in verificadores:
        if verificador < numero:
            aux_verificadores.append(verificador)
    aux_verificadores.sort(reverse=True)

    for verificador in aux_verificadores:
        condicao = soma + verificador
        if condicao <= numero:
            resultado.append(verificador)
            soma += verificador
    palavra_calculada[numero] = resultado


def eh_verificador(numero):
    while numero >= 1 and numero % 2 == 0:
        numero /= 2
    return numero == 1


if __name__ == '__main__':
    main()
