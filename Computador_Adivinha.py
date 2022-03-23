from random import randint
from time import sleep #make the computador sleep
class bcolors:
    FAIL= '\033[91m' #RED
    SUCCESS= '\033[92m' #GREEN
computador= randint(0,5)#Pega o número aleatório entre 0 a 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar....')
print('-=-' * 20)
jogador= int(input('Em qual número eu pensei?')) #Jogador tenta adivinhar
print('loading.....')
sleep(1)
if jogador==computador:
    print(f'{bcolors.SUCCESS}Você acertou parabêns!!!! Pensei no número: {computador}')
else:
    print(f'{bcolors.FAIL}Você errou, pensei no número: {computador} e você achou que era: {jogador}')