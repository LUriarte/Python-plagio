# Programa para a detecção de plágio

import re

def main():
    ass_controle = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos, ass_controle)
    
    print('O autor do texto', infectado, 'está infectado com COH-PIAH')

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print()
    print("Informe a assinatura típica de um aluno infectado:")
    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    print()
    ass_controle = [wal, ttr, hlr, sal, sac, pal]

    return ass_controle

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
        print()

    return textos

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_assinaturas = []
    for i in range(len(textos)):
        lista_assinaturas.append(calcula_assinatura(textos[i]))
    
    lista_semelhancas = []
    for i in range(len(lista_assinaturas)):
        lista_semelhancas.append(compara_assinatura(lista_assinaturas[i], ass_cp))
    
    infectado = min(lista_semelhancas)
    infectado_index = lista_semelhancas.index(infectado)
    infectado_index += 1
    
    return infectado_index
    
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    wal_final = abs(as_a[0] - as_b[0]) 
    ttr_final = abs(as_a[1] - as_b[1])
    hlr_final = abs(as_a[2] - as_b[2])
    sal_final = abs(as_a[3] - as_b[3])
    sac_final = abs(as_a[4] - as_b[4])
    pal_final = abs(as_a[5] - as_b[5])
    semelhanca = (wal_final + ttr_final + hlr_final + sal_final + sac_final + pal_final) / 6

    return semelhanca

# Funções para calcular a assinatura________________________________________________

def calcula_assinatura(texto):
    '''Função principal para calcular assinatura'''
    
    # SAL – Tamanho médio da sentença – soma do número de caracteres em todas as senteças / número de sentenças
    sentencas = separa_sentencas(texto)
    num_sentencas = len(sentencas)
    num_caracteres_sentencas = 0
    for n in sentencas:
        num_caracteres_sentencas += len(n)
    sal = num_caracteres_sentencas / num_sentencas

    # SAC – Complexidade da sentença. Número total de frases / número de sentenças
    lista_lista = []
    for n in sentencas:
        lista_lista.append(separa_frases(n))
    lista_frases = []
    for sublista in lista_lista:
        for n in sublista:
            lista_frases.append(n)
    num_frases = len(lista_frases)
    sac = num_frases / num_sentencas

    # PAL – Tamanho médio da frase. número de caracteres em cada frase / número total de frases
    carac_frases = 0
    for n in lista_frases:
        carac_frases += len(n)
    pal = carac_frases / num_frases

    # TTR – Relação Type-Token. número de palavras diferentes / número total de palavras
    lista_lista2 = []
    for n in lista_frases:
        lista_lista2.append(separa_palavras(n))
    lista_palavras = [i for sublista in lista_lista2 for i in sublista]
    num_palavras_diferentes = n_palavras_diferentes(lista_palavras)
    num_palavras = len(lista_palavras)
    ttr = num_palavras_diferentes / num_palavras

    # HLR – Relação Hapax Legomana. número de palavras utilizadas uma única vez / número total de palavras
    num_palavras_unicas = n_palavras_unicas(lista_palavras)
    hlr = num_palavras_unicas / num_palavras
        
    # WAL – Tamanho médio de palavra. Soma len(palavras) / número total de palavras
    caracteres_palavras = 0
    for n in lista_palavras:
        caracteres_palavras += len(n)
    wal = caracteres_palavras / num_palavras

    ass = [wal, ttr, hlr, sal, sac, pal]

    return ass

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]

    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''

    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''

    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


# Fim das funções para calcular assinatura___________________________________________
