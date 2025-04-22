# Este é um arquivo com as funções que eu utilizo no código. 

import string, random 


def gerar_codigo():

    letras_maiusculas, letras_minusculas = string.ascii_uppercase, string.ascii_lowercase

    letras = list(letras_maiusculas + letras_minusculas)

    codigo = ""
    digitos_gerado = 0
    while digitos_gerados < 5:
        numero = random.randint(0, 100000)

        if numero % 2 == 0:
            digito_numerico = random.randint(0, 10)
            codigo += str(digito_numerico)
            digitos_gerado += 1

        else:
            random.shuffle(letras)
            letra = random.choice(letras)
            codigo += letra 

            letras.remove(letra) 

            digitos_gerado += 1


    return codigo




