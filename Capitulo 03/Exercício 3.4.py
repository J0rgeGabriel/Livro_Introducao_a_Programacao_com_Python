#Escreva uma expressão para determinar se uma pessoa deve ou não
#pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
#R$ 1.200,00.

salario = float(input("Digite o seu salario: R$"))
if salario > 1200:
    print("Você deve pagar imposto!")
else:
    print("Você não precisa pagar imposto")