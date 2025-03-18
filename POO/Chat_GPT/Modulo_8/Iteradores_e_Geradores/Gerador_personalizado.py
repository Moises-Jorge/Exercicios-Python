def pares(n):
    for num in range(0, n+1, 2):
        yield num
        
        
# teste
for num in pares(10):
    print(num, end=' ')