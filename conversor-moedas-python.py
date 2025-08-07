# Conversor de Moedas entre 10 principais moedas internacionais

taxas = {
    'USD': {'EUR': 0.92, 'GBP': 0.78, 'JPY': 146.9, 'CHF': 0.88, 'AUD': 1.52, 'CAD': 1.34, 'CNY': 7.29, 'INR': 83.0, 'BRL': 5.20},
    'EUR': {'USD': 1.09, 'GBP': 0.85, 'JPY': 159.3, 'CHF': 0.96, 'AUD': 1.65, 'CAD': 1.46, 'CNY': 7.94, 'INR': 90.2, 'BRL': 5.65},
    'GBP': {'USD': 1.28, 'EUR': 1.17, 'JPY': 187.2, 'CHF': 1.13, 'AUD': 1.94, 'CAD': 1.72, 'CNY': 9.33, 'INR': 105.6, 'BRL': 6.55},
    'JPY': {'USD': 0.0068, 'EUR': 0.0063, 'GBP': 0.0053, 'CHF': 0.006, 'AUD': 0.010, 'CAD': 0.0092, 'CNY': 0.050, 'INR': 0.56, 'BRL': 0.035},
    'CHF': {'USD': 1.14, 'EUR': 1.04, 'GBP': 0.89, 'JPY': 167.2, 'AUD': 1.72, 'CAD': 1.51, 'CNY': 8.28, 'INR': 93.8, 'BRL': 5.80},
    'AUD': {'USD': 0.66, 'EUR': 0.61, 'GBP': 0.52, 'JPY': 97.3, 'CHF': 0.58, 'CAD': 0.88, 'CNY': 4.80, 'INR': 54.5, 'BRL': 3.38},
    'CAD': {'USD': 0.75, 'EUR': 0.68, 'GBP': 0.58, 'JPY': 110.6, 'CHF': 0.66, 'AUD': 1.14, 'CNY': 5.43, 'INR': 62.0, 'BRL': 3.85},
    'CNY': {'USD': 0.14, 'EUR': 0.13, 'GBP': 0.11, 'JPY': 20.5, 'CHF': 0.12, 'AUD': 0.21, 'CAD': 0.18, 'INR': 11.4, 'BRL': 0.71},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095, 'JPY': 1.78, 'CHF': 0.011, 'AUD': 0.018, 'CAD': 0.016, 'CNY': 0.088, 'BRL': 0.062},
    'BRL': {'USD': 0.19, 'EUR': 0.18, 'GBP': 0.15, 'JPY': 28.4, 'CHF': 0.17, 'AUD': 0.30, 'CAD': 0.26, 'CNY': 1.41, 'INR': 16.1}
}

moedas = list(taxas.keys())

def exibir_menu():
    print("\n" + "="*40)
    print("       CONVERSOR DE MOEDAS 🌍")
    print("="*40)
    for idx, moeda in enumerate(moedas):
        print(f"{idx + 1}. {moeda}")
    print("="*40)

def obter_moeda(mensagem):
    while True:
        try:
            escolha = int(input(mensagem))
            if 1 <= escolha <= len(moedas):
                return moedas[escolha - 1]
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Digite um número válido.")

def main():
    while True:
        exibir_menu()
        origem = obter_moeda("Escolha a moeda de origem (1-10): ")
        destino = obter_moeda("Escolha a moeda de destino (1-10): ")

        if origem == destino:
            print("As moedas são iguais. Nada para converter.")
            continue

        try:
            valor = float(input(f"Digite o valor em {origem}: "))
        except ValueError:
            print("Valor inválido.")
            continue

        taxa = taxas.get(origem, {}).get(destino)

        if taxa:
            convertido = valor * taxa
            print(f"\n💱 {valor:.2f} {origem} = {convertido:.2f} {destino}")
        else:
            print("Conversão não disponível.")

        repetir = input("\nDeseja converter outro valor? (s/n): ").lower()
        if repetir != 's':
            print("\nObrigado por usar o conversor de moedas Python! 💸")
            break

if __name__ == "__main__":
    main()
