print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 18

chute = input('Digite um número')

print('Você digitou o número', chute)

if numeroSecreto == chute:
    print('Você acertou!')

else:
    print('Vocẽ errou!')