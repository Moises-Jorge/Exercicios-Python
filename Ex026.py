''' programa que leh uma frase pelo teclado e mostre:
    a) Quantas vezes aparece a letra “A”;
    b) Em que posição ela aparece pela primeira vez;
    c) Em que posição ela aparece pela última vez
'''
frase = str(input('Digite uma frase: '))

print('Quantas vezes aparece a letra "A"?: ', frase.count('a'))
print('Em que posição aparece pela primeira vez?: ', frase.find('a') + 1)
print('Em que posição aparece pela ultima vez?: ', frase.rfind('a') + 1)