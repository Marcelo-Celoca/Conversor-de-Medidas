def celsius_para_fahrenheit(celsius):
    resultado = (celsius * 1.8) + 32
    return resultado 

def metros_para_centimetros(metros):
    return metros * 100 

print("--- ⚖️ CONVERSOR DE MEDIDAS ---")

while True:
    print("\nMENU:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Metros para Centímetros")
    print("3 - Sair")

    try:
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            valor = float(input("Digite a temperatura em °C: "))
            f = celsius_para_fahrenheit(valor)
            print(f"🔥 Resultado: {f:.2f}°F")

        elif opcao == 2:
            valor = float(input("Digite o valor em metros: "))
            print(f"📏 Resultado: {metros_para_centimetros(valor)} cm")

        elif opcao == 3:
            print("Encerrando o conversor...")
            break
        else:
            print("⚠️ Opção inválida!")

    except ValueError:
        print("❌ Erro: Por favor, digite apenas números.")
