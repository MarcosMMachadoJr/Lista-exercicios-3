N = int(input("Digite o número de jogadores: "))

saquetotal = 0
bloqtotal = 0
ataquetotal = 0
saquestotalSucesso = 0
bloctotalSucesso = 0
ataquetotalSucesso = 0

for i in range(N):
    # Nome do jogador
    nome = input(f"Digite o nome do jogador {i + 1}: ")

    # Recebendo os dados de tentativas
    S, B, A = map(int, input("Digite as tentativas de saques, bloqueios e ataques: ").split())
    # Recebendo os dados de sucessos
    S1, B1, A1 = map(int, input("Digite os sucessos de saques, bloqueios e ataques: ").split())

    # Somando as tentativas para todos os jogadores
    saquetotal += S
    bloqtotal += B
    ataquetotal += A

    # Somando os sucessos para todos os jogadores
    saquestotalSucesso += S1
    bloctotalSucesso += B1
    ataquetotalSucesso += A1

# Calculando os percentuais de sucesso
percentual_saques = (saquestotalSucesso / saquetotal) * 100 if saquetotal > 0 else 0
percentual_bloqueios = (bloctotalSucesso / bloqtotal) * 100 if bloqtotal > 0 else 0
percentual_ataques = (ataquetotalSucesso / ataquetotal) * 100 if ataquetotal > 0 else 0

# Exibindo os resultados
print(f"Percentual de sucesso de saques: {percentual_saques:.2f} %")
print(f"Percentual de sucesso de bloqueios: {percentual_bloqueios:.2f} %")
print(f"Percentual de sucesso de ataques: {percentual_ataques:.2f} %")
