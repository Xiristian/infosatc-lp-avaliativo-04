dadosCadastrais = ""
pessoasCadastradas = 0

while pessoasCadastradas < 5:
    idade = int(input("Quantos anos você tem? "))
    peso = int(input("Quantos quilos você tem? "))
    horaSono = int(input("Aproximadamente, quantas horas de sono você teve nas últimas 24 horas? "))

    def confirmar(idade,peso,sono):
        idadeErrada = ""
        pesoErrado = ""
        sonoErrado = ""

        if idade > 15 and idade < 70 and peso > 50 and horaSono >= 6:
            return True

        if idade <= 15 or idade >= 70:
            idadeErrada = "\n(X)Idade fora do intervalo de 16 e 69 anos;"
        else:
            idadeErrada = "\n( )Idade fora do intervalo de 16 e 69 anos;"

        if peso <= 50:
            pesoErrado = "\n(X)Peso abaixo de 50kg;"
        else:
            pesoErrado = "\n( )Peso abaixo de 50kg;"

        if horaSono < 6:
            sonoErrado = "\n(X)Horas de sono das últimas 24 horas abaixo de 6;"
        else:
            sonoErrado = "\n( )Horas de sono das últimas 24 horas abaixo de 6;"

        return idadeErrada + pesoErrado + sonoErrado

    if confirmar(idade,peso,horaSono) == True:
        apto = "Está apto para doar sangue"
        print(apto)
    else:
        apto = "Não está apto para doar sangue"
        print(apto)
        print("Motivos: ", confirmar(idade,peso,horaSono))


    def cadastro():
        cadastro = input("Você deseja se cadastrar no nosso laboratório?(S/N) ")
        if cadastro == "S":
            return True
        return False


    if cadastro() == True:
        pessoasCadastradas += 1
        nome = input("Digite seu nome completo: ")
        cpf = input("Digite seu CPF: ")
        senha = input("Digite sua senha: ")

        dadosCadastrais = dadosCadastrais + f"\n{pessoasCadastradas}° Pessoa cadastrada:\nNome: " + nome + "\nCpf: " + cpf + "\nSenha: " + senha + "\n" + apto
        print("Cadastrado com sucesso!")


print(dadosCadastrais)