'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. '''
expressao = str(input('Digite uma expressao: ')) # (a+b)(a+c))
pilha = list()
for caracter in expressao:
    if caracter == '(':
        pilha.append(caracter)
    elif caracter == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(caracter) # Estah a se add esse char na pilha para na verificacao final o tamanho da pilha ser diferente de zero e exibir o erro!
            break
if len(pilha) == 0:
    print('Sua expressao estah valida!')
else:
    print('Sua experssao estah errada!')