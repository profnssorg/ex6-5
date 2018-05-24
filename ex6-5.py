"""
Programa exercicio6-5.
Descrição: Este programa é o exercício 5 do capítulo 6 de Menezes (2004, p.109).  Trata-se da simulação de uma fila de banco.
Autor: Nelson S. dos Santos
Data: 23/05/2018
Versão: 1.0.0
"""

# Inicialização de variáveis

ultimo = 10
fila = list(range(1, ultimo +1))
operacao = ''

# Entrada, processamento e saída

#while True:
print('Digite uma sequência cujos elementos só podem ser as letras F, A ou S. F adiciona um cliente ao fim da fila,')
print('A realiza o atendimento. S para sair.')
operacao = input('A sequência de elementos é: ')
for letra in operacao:
    print('\nExistem %d clientes na fila'%len(fila))
    print('Fila atual: ', fila)
    
    if letra != 'A':
        if letra != 'F':
            if letra != 'S':
                print('A sequência de operações só pode conter F, A ou S.')
    elif letra == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print('Cliente %d atendido' %atendido)
        else: 
            print('Fila vazia. Ninguém para atender.')
    elif letra == 'F':
        ultimo +=1 # incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif letra == 'S':
        break
   