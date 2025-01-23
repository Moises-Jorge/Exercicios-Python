# Empacotando
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')


# Desempacotando
def soma(* num):
    s = 0
    for n in num:
        s += n
    print(f'Somando os numeros {num} temos {s}')
    

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


# Programa Principal
valores = [1, 2, 3, 4, 5]
print(valores)
dobra(valores)
print(valores)
soma(4, 5)
soma(4, 5, 6)
