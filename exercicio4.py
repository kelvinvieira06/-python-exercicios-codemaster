idade = int(input("Insire a sua idade: "))

if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")

if idade > 0 and idade < 13:
    print("Criança")

elif idade >= 13 and idade <= 17:
    print("Adolescente")

elif idade >= 18:
    print("Adulto")

else:
    print("idade invalida!")

print(" ")

#complete