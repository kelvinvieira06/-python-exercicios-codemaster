num1 = float(input("Primeiro numero: "))
op = input("Escolha uma operação(+; -; x; /): ")
num2 = float(input("Segundo numero: "))

if op == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif op == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif op == "x" or "*":
    resultado = num1 * num2
    print(f"{num1} x {num2} = {resultado}")

elif op == "/":
    if num2 == 0:
        print("Não divide por 0 mano!")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
else:
    print(f"Operação invalida!")


#incomplete