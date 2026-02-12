""" Adivinhe o número """

from random import randint
""" Biblioteca do random, somente a aparte de gera números aleátorios """

def linhas(txt): # somente pra ficar uma linha mais clean no final
    print('~' * len(txt))
    
    
 # print(sorte) macete pra saber a resposta(recomendo deixar comentado pra não roubar hehe)
def tente_sua_sorte():
    sorte = randint(1, 10) # gera o numero aleatório
    tentativa = 0 # usuario começa com zero, ja que não jogou ainda
    acertou = False # falso porque ele ainda não jogou
    # print(sorte)
    
    while not acertou: # loop pra pecorrer até ele acertar
        try: 
            
            adivinhe = int(input("Tente a sorte: ")) # input pro usúario digitar o número
            tentativa += 1
            if adivinhe == sorte: # se ele acertar o número, aparece mensagem de acerto

                print("Parabéns, Você Acertou!!!")
                print(f"Você teve {tentativa} tentativas.")
                acertou = True
              
            elif adivinhe < sorte:
                print("Tente um número maior.")
                
            else:
              print("Tente um número menor.")
              
        except ValueError:
            print("erro 400: Digite somente números inteiros!")


if __name__=="__main__":
    
    txt = 'Adivinhe o número'
    
    print(txt)
    
    linhas(txt)
    tente_sua_sorte()
    linhas(txt)