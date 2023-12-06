def form():
    while True:
        nome = input('Qual o seu nome? (Digite "0" para encerrar)')
        if nome == "0":
            break

        arquivo = open('meu_arquivo.txt', 'a', encoding='utf-8')  
        arquivo.write(nome)
        arquivo.write("|")

        idade = input('Qual a sua idade?')
        arquivo.write(idade)
        arquivo.write("|")

        sexo = input('Qual o seu sexo?')
        arquivo.write(sexo)
        arquivo.write("|")
        
        telefone = input('Qual o seu telefone?')
        arquivo.write(telefone)
        arquivo.write('\n')
        arquivo.close()

form()

def ler():
    arquivo = open('meu_arquivo.txt', 'r', encoding='utf-8')
    print(arquivo.read())
