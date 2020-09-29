palavra = input("Digite uma palavra: ")

def inverter(palavra):
    invertida = ""

    for i in palavra:
        invertida = i + invertida
    print(invertida)

inverter("Palavra invertida: ", palavra)