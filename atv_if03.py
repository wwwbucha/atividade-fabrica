a = float(input("Digite a primemira nota: "))
b = float(input("Digite a segunda nota: "))

resultado = (a+b)/2
print("sua media é: %0.2f"%(resultado))

if resultado>7:
    print("APROVADO.")
elif (resultado>=5)and(resultado<=6.99):
    print("em recuperação")
else:
    print("reprovado")