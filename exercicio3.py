#formula para converter ºC para ºF é (ºC x 1.8) + 32
# 
#formula para converter ºF para ºC é (ºF - 32) x 1.8

udm = (input("Converter a temperatura para C ou F? "))
temp = float(input("Temperatura: "))

if udm.upper() == "C":
    resultado = (temp - 32) * 5/9
    print(f"{temp}ºF em ºC é {resultado: .2f}ºC")

elif udm.upper() == "F":
    resultado = (temp * 1.8) + 32
    print(f"{temp}ºC em ºF é {resultado: .2f}ºF")
else:
    print("Unidade de medida invalida!")


#complete