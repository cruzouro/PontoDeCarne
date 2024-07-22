####### V1 22/07/2024
####### Daniele Cruz

try:
    point = int(input('Insira a temperatura da carne em Cº: '))
except:
    print('Tente novamente utilizando valores numericos')
else:
    if point >= 48 and point <= 53:
        print(f'Mal Passado')
    elif point >= 54 and point <= 59:
        print(f'Ao ponto para mal passado')
    elif point >= 60 and point <= 64:
        print(f'Ao ponto')
    elif point >= 65 and point <= 69:
        print(f'Ao Ponto para bem passado')
    elif point >= 70 and point <= 89:
        print(f'Bem passado')    
    elif point >= 80:
         print(f'Passado')
    elif point <= 47:
        print(f'A carne está Crua')

        