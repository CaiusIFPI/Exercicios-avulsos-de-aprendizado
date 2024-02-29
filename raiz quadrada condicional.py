from math import sqrt

num = int(input('Vamos verificar se um número possui raíz quadrada inteira, digite um número: '))
raiz = sqrt(num)
if raiz.is_integer():
    print(f'A raíz de {num} é {raiz:.0f}.')
else:
    print('Este número não possui raíz quadrada inteira.')