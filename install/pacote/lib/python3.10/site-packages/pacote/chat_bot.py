import re
import os
def guiar(local,position):
    return "preparando  para guiar ate "+local+" na posição "+str(position)
def encontrar(local,position):
    return local+" fica na posição "+str(position)
def ir(local,position):
    return "indo para "+local+" na posição "+str(position)


def main():
    places = {
        "biblioteca": (0,0),
        "garagem": (1,2),
        "fazol" : (3,3)
    }
    funcoes = {
        "dirigir": ir,
        "encontar": encontrar,
        "ir": ir,
        "mover": ir,
        "guiar": ir,
        "conduzir": guiar
    }

    while True:
        text =input("ensira o local que deseja ir, se desejar ver a lista de locais digite 1, se quiser sair digite exit: ").strip().lower()
        
        if text=="exit":
            break

        if text=="1":
            response = "os lugares são: "
            for place in places.keys():
                response += f"{place}, "
            response = response[:-2]+"."
            print(response)
            continue
                                        

        action_regex = "(?:diri(gir|ja))|(?:conduz(ir|a))|(?:movimentar)|(?:mov(er|a))|(?:encontr(ar|e))|(?:gui(ar|e))|(?:ir)|"
        action_match = re.search(action_regex, text)



        place_regex = "(?:biblioteca){1}|(?:garagem){1}|(?:fazol){1}"
        place_match = re.search(place_regex, text)
        
        if action_match:
            if place_match :
        
                
                response = funcoes[action_match.group(0)](place_match.group(0),places[place_match.group(0)])
                print(response)
                
            else:
                response = "não entendi para onde você quer ir"


                print(response)
        else:
            print("não entendi o que você disse")
        


if __name__ == '__main__':
    main()  


