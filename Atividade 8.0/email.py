def valida_email(email):
    return email[-8:] =="@puc.com"


def tamanho8(senha):
    if (len(senha) < 8):
         print("Necessario ter mais que 8 caracteres !")
         return
    else:
        return True
def verifica_maiuscula(senha):
    for letra in senha:
        if letra.isupper():
            return True
    print("Necessario pelo menos 1 caractere maiuscula !")
    return False

def verifica_minuscula(senha):
    for letra in senha:
        if letra.islower():
            return True
    print("Necessario pelo menos 1 caractere minuscula !")
    return False

def verifica_num(senha):
    for letra in senha:
        if '0' <= senha <= '9':
            return True
    print("Necessario pelo menos 1 numero !")
    return False


def valida_senha(senha):
    tamanho8 = len(senha) >= 8
    possuiMaiuscula = verifica_maiuscula(senha)
    possuiMinuscula = verifica_minuscula(senha)
    possuiNumero = verifica_num(senha)

    return tamanho8 and possuiMaiuscula and possuiMinuscula and possuiNumero

valida_senha("abc@1234")
    





        