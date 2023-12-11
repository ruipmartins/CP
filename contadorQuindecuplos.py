# Define o nome do arquivo
nome_arquivo = "estelas.txt"

# Inicializa um dicionário para armazenar a contagem de quindecuplos
contagem_quindecuplos = {}

# Lê o arquivo e processa cada linha
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        # Remove caracteres de quebra de linha
        linha_limpa = linha.strip()

        # Divide a linha em quindecuplos e conta as ocorrências
        quindecuplos = linha_limpa.split('-')
        for i in range(len(quindecuplos) - 14):
            quindecuplo = f"{quindecuplos[i]}-{quindecuplos[i+1]}-{quindecuplos[i+2]}-{quindecuplos[i+3]}-{quindecuplos[i+4]}-{quindecuplos[i+5]}-{quindecuplos[i+6]}-{quindecuplos[i+7]}-{quindecuplos[i+8]}-{quindecuplos[i+9]}-{quindecuplos[i+10]}-{quindecuplos[i+11]}-{quindecuplos[i+12]}-{quindecuplos[i+13]}-{quindecuplos[i+14]}"
            if len(quindecuplo) > 29:
                contagem_quindecuplos[quindecuplo] = contagem_quindecuplos.get(quindecuplo, 0) + 1

# Ordena os quindecuplos pela quantidade de ocorrências
quindecuplos_ordenados = sorted(contagem_quindecuplos.items(), key=lambda x: x[1], reverse=True)

total_contagem = sum(contagem for quindecuplo, contagem in quindecuplos_ordenados)

print("\nContagens de quindecuplos de caracteres com mais do que uma ocorrência:")

# Imprime o resultado ordenado com a porcentagem relativa
for quindecuplo, contagem in quindecuplos_ordenados:
    if contagem > 1 and len(quindecuplo) > 29:
        porcentagem = (contagem / total_contagem) * 100 if total_contagem != 0 else 0
        print(f"Quindecuplo: {quindecuplo}, Contagem: {contagem}, Porcentagem: {porcentagem:.2f}%")
