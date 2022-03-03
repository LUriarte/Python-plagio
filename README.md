# Python-plagio
Detector de plágio desenvolvido em Python – projeto final do curso de Introdução à Ciência da Computação com Python parte 1, oferecido pela USP na plataforma Coursera

* Ferramentas utilizadas
  - Linguagem de programação Python

* Metodologia
  - Criação de um programa de detecção de plágio a partir do cálculo e comparação de diversos elementos textuais como: 
    - tamanho médio de sentença
    - complexidade da sentença
    - tamanho médio da frase
    - relação type/tokien
    - relação Hapax Legomana
    - tamanho médio da palavra
  - A estrutura do programa compreende diversas funções, responsáveis pelo input dos textos, cálculo de cada um dos elementos textuais, chegando a um valor chamado "assinatura do texto". As assinaturas dos textos são comparadas, sendo que, quanto menor a diferença entre as mesmas, maior a chance de plágio (se a diferença for zero, a cópia é idêntica)   
    
