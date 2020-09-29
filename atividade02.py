palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite uma palavra para saber se é o inverso da anterior: ")

def inverter(palavra):
    invertida = ""

    for i in palavra:
        invertida = i + invertida
    print(invertida)
    return invertida

print(palavra2)

if inverter(palavra1) == palavra2:
    print("As palavras são o inverso uma da outra")
else:
    print("As palavras não são o inverso uma da outra")