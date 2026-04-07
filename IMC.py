def calcular_imc (peso, altura):
    """Calcula o IMC com base no peso e altura."""
    return peso / (altura ** 2)

def classificar_imc (imc):
    if imc < 18.5:
        return ("Você está abaixo do peso")
    elif imc < 25:
        return ("Você está no peso ideal")
    elif imc < 30:
        return ("Você está acima do peso")
    elif imc < 35:
        return ("Você está com obesidade grau 1")
    elif imc < 40:
        return ("Você está com obesidade grau 2")
    else:
        return ("Você está com obesidade grau 3")
    
def obter_dados():
    while True:
        try:
            peso = float(input("Informe o peso em kg: "))
            altura = float(input("Informe a altura em metros: "))

            if peso <= 0 or altura <= 0:
                print("Peso e altura devem ser maiores que 0.\n")
                continue

            return peso, altura
        
        except ValueError:
            print("Digite apenas números. (Utilize . para separar a casa decimal)\n")

def main():
    peso, altura = obter_dados()
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"\nSeu IMC é: {imc:.2f}")
    print(classificacao)

if __name__ == "__main__":
    while True:
        main()
        repetir = input("\nDeseja calcular novamente? (s/n): ").lower().strip()
        if repetir != 's':
            break