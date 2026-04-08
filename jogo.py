jogador1 = int(input('Informe um número: '))
jogador2 = int(input('Informe outro número: '))

soma = jogador1 + jogador2

if soma % 2 == 0:
    print(f'A soma {soma} é par')
else:
    print(f'A soma {soma} é ímpar')
#lógica - if e else 
if soma % 2 != 0:
    print('impar ganhou')
else:
    print('par ganhou')