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

def ler_dados():
    arquivo = open('meu_arquivo.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        dados = linha.strip().split('|')

        nome = dados[0]
        idade = dados[1] + " anos"
        sexo = "Masculino" if dados[2] == 'M' else "Feminino"
        telefone = dados[3]

        print(f"• Nome: {nome}")
        print(f"• Idade: {idade}")
        print(f"• Sexo: {sexo}")
        print(f"• Telefone: {telefone}")
        print()

form()
ler_dados()
