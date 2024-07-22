####### V1 22/07/2024
####### Daniele Cruz

try:
    point = int(input('Insira a temperatura da carne em Cº: '))
except:
    print('Tente novamente utilizando valores numericos')
else:
    if point >= 48 and point <= 53:
        print(f'\nMal Passado')
    elif point >= 54 and point <= 59:
        print(f'\nAo ponto para mal passado')
    elif point >= 60 and point <= 64:
        print(f'\nAo ponto')
    elif point >= 65 and point <= 69:
        print(f'\nAo Ponto para bem passado')
    elif point >= 70 and point <= 89:
        print(f'\nBem passado')    
    elif point >= 80:
         print(f'\nPassado')
    elif point <= 47:
        print(f'\nA carne está Crua')

        