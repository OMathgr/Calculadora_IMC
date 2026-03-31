def calcular_imc (peso, altura):
    return peso / (altura ** 2)

def classificar_imc (imc):
    if imc < 18.5:
        return ("Você está abaixo do peso")
    elif imc < 25:
        return ("Você está no peso ideal")
    elif imc < 30:
        return ("Você está acima do peso")
    else:
        return ("Você está com obesidade")

try:
    peso = float(input("Informe o peso em kg: "))
    altura = float(input("Informe a altura em metros: "))

    imc = calcular_imc(peso,altura)
    classificacao = classificar_imc(imc)

    print (f"Seu IMC é: {imc:.2f}")
    print (classificacao)

except ValueError:
    print ("Erro: Digite apenas números.")

except ZeroDivisionError:
    print ("Erro: A altura não pode ser igual a zero.")