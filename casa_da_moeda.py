
import requests

# 1. BUSCAR AS TAXAS ATUALIZADAS
url = "https://v6.exchangerate-api.com/v6/3498b24e48d05c3cbba5e638/latest/USD"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()
        taxas = data["conversion_rates"]

        print("Taxas de câmbio atualizadas em tempo real!")

    else:
        print(f"Erro na API. Status: {response.status_code}")
        exit()

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")
    exit()


# INTERFACE INICIAL
print("=" * 50)
print("          Bem vindo a Casa da moeda!")
print("=" * 50)


# 2. CRIAR O CATÁLOGO AUTOMATICAMENTE
moedas = list(taxas.keys())


# 3. CRIAR O MENU
def menu():
    print("\n===== MOEDAS DISPONÍVEIS =====")

    for numero, codigo in enumerate(moedas, 1):
        print(f"{numero} - {codigo}")


# 4. ESCOLHA DA MOEDA DE ORIGEM
menu()

while True:
    try:
        moeda_origem = int(
            input("\nQual moeda voce deseja converter inicialmente? ")
        )

        if 1 <= moeda_origem <= len(moedas):
            break

        print("Escolha uma opcao valida.")

    except ValueError:
        print("Digite apenas um numero.")


# Código da moeda de origem
code_origem = moedas[moeda_origem - 1]

# 5. QUANTIA
while True:
    try:
        quantia = float(
            input(f"Quantia em {code_origem}: ")
        )

        if quantia >= 0:
            break

        print("Digite um valor positivo.")

    except ValueError:
        print("Digite apenas numeros.")


# 6. ESCOLHA DA MOEDA DE DESTINO
menu()

while True:
    try:
        moeda_destino = int(
            input("\nPara qual moeda voce deseja converter? ")
        )

        if 1 <= moeda_destino <= len(moedas):
            break

        print("Escolha uma opcao valida.")

    except ValueError:
        print("Digite apenas um numero.")


# Código da moeda de destino
code_destino = moedas[moeda_destino - 1]


# 7. CONVERSÃO
if code_origem == code_destino:

    print(f"\nA moeda ja esta em {code_origem}.")

else:

    # Transformar a moeda de origem em USD
    quantia_em_usd = quantia / taxas[code_origem]

    # Transformar USD na moeda de destino
    final = quantia_em_usd * taxas[code_destino]

    # Resultado
    print("\n" + "=" * 50)
    print("             RESULTADO")
    print("=" * 50)

    print(
        f"Voce converteu {quantia:.2f} {code_origem} "
        f"em {final:.2f} {code_destino}!"
    )

    print("=" * 50)
