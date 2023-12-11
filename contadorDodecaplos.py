# Define o nome do arquivo
nome_arquivo = "estelas.txt"

# Inicializa um dicionário para armazenar a contagem de dodecaplos
contagem_dodecaplos = {}

# Lê o arquivo e processa cada linha
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        # Remove caracteres de quebra de linha
        linha_limpa = linha.strip()

        # Divide a linha em dodecaplos e conta as ocorrências
        dodecaplos = linha_limpa.split('-')
        for i in range(len(dodecaplos) - 11):
            dodecaplo = f"{dodecaplos[i]}-{dodecaplos[i+1]}-{dodecaplos[i+2]}-{dodecaplos[i+3]}-{dodecaplos[i+4]}-{dodecaplos[i+5]}-{dodecaplos[i+6]}-{dodecaplos[i+7]}-{dodecaplos[i+8]}-{dodecaplos[i+9]}-{dodecaplos[i+10]}-{dodecaplos[i+11]}"
            if len(dodecaplo) > 23:
                contagem_dodecaplos[dodecaplo] = contagem_dodecaplos.get(dodecaplo, 0) + 1

# Ordena os dodecaplos pela quantidade de ocorrências
dodecaplos_ordenados = sorted(contagem_dodecaplos.items(), key=lambda x: x[1], reverse=True)

total_contagem = sum(contagem for dodecaplo, contagem in dodecaplos_ordenados)

print("\nContagens de dodecaplos de caracteres com mais do que uma ocorrência:")

# Imprime o resultado ordenado com a porcentagem relativa
for dodecaplo, contagem in dodecaplos_ordenados:
    if contagem > 1 and len(dodecaplo) > 23:
        porcentagem = (contagem / total_contagem) * 100 if total_contagem != 0 else 0
        print(f"Dodecaplo: {dodecaplo}, Contagem: {contagem}, Porcentagem: {porcentagem:.2f}%")
