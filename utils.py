import dados

def ler_numero_quebrado(texto):
    while True:
        try:
            n = float(input(texto))
            return n
        except ValueError:
            print("Erro: digite um numero valido")

def ler_numero_inteiro(texto):
    while True:
        try:
            n = int(input(texto))
            return n
        except ValueError:
            print("Erro: digite um numero inteiro valido")

def valida_cpf(numero_cpf):
    if len(numero_cpf) != 11 or not numero_cpf.isdigit():
        print("Cpf incorreto. Precisa ter 11 digitos e so numeros")
        return False
    if numero_cpf in dados.cpfs_existentes:
        print("Erro: Cpf existente")
        return False
    return True

def pegador(lista_geral):
    for registro in lista_geral:
        yield registro

def gera_id_cliente(nome, cpf):
    letras = nome[:3].upper()
    numeros = cpf[-4:]
    retorno_id = letras + "-" + numeros
    return retorno_id