'''Escreva uma expressão que será utilizada para decidir se um aluno foi
ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores
que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.'''


prova01 = float(input("Digite a nota que você tirou na prova 01: ").replace(",","."))
while prova01 < 0 or prova01 > 10:
    prova01 = float(input("Valor invalido! Digite a nota que você tirou na prova 01: ").replace(",", "."))

prova02 = float(input("Digite a nota que você tirou na prova 02: ").replace(",", "."))
while prova02 < 0 or prova02 > 10:
    prova02 = float(input("Valor invalido! Digite a nota que você tirou na prova 02: ").replace(",", "."))

prova03 = float(input("Digite a nota que você tirou na prova 03: ").replace(",", "."))
while prova03 < 0 or prova03 > 10:
    prova03 = float(input("Valor invalido! Digite a nota que você tirou na prova 03: ").replace(",", "."))

notas = prova01 + prova02 + prova03
media = round(notas / 3, 2)

if media > 7:
    print(f"Parabens, voce foi aprovado, sua media foi de {media}")
else:
    print(f"Voce foi reprovado, sua media foi de {media}")
