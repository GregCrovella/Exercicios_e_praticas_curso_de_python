
senha_secreta = '153196'
numeros_acertados = ''
numero_tentativas = 0

while True:

    numeros_digitados = input('Digite um número: ')
    numero_tentativas += 1

    if len(numeros_digitados) > 1:
        print('Digite apenas um número!')
        continue

    if numeros_digitados in senha_secreta:
        numeros_acertados += numeros_digitados

    numero_formado = ''
    for numero_secreto in senha_secreta:
        if numero_secreto in numeros_acertados:
            numero_formado += numero_secreto

        else:
            numero_formado += '*'

    print('Número formado:', numero_formado)

    if numero_formado == senha_secreta:
        print('!!!PARABÉNS, VOCÊ ACERTOU A SENHA SECRETA!!!')
        print('A senha era: ', senha_secreta)
        print('Tentaivas: ', numero_tentativas)
        numeros_acertados = ''
        numero_tentativas = 0
