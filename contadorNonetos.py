# Define o nome do arquivo
nome_arquivo = "estelas.txt"

# Inicializa um dicionário para armazenar a contagem de nonetos
contagem_nonetos = {}

# Lê o arquivo e processa cada linha
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        # Remove caracteres de quebra de linha
        linha_limpa = linha.strip()

        # Divide a linha em nonetos e conta as ocorrências
        nonetos = linha_limpa.split('-')
        for i in range(len(nonetos) - 8):
            noneto = f"{nonetos[i]}-{nonetos[i+1]}-{nonetos[i+2]}-{nonetos[i+3]}-{nonetos[i+4]}-{nonetos[i+5]}-{nonetos[i+6]}-{nonetos[i+7]}-{nonetos[i+8]}"
            if len(noneto) > 17:
                contagem_nonetos[noneto] = contagem_nonetos.get(noneto, 0) + 1

# Ordena os nonetos pela quantidade de ocorrências
nonetos_ordenados = sorted(contagem_nonetos.items(), key=lambda x: x[1], reverse=True)

total_contagem = sum(contagem for noneto, contagem in nonetos_ordenados)

print("\nContagens de nonetos de caracteres com mais do que uma ocorrência:")

# Imprime o resultado ordenado com a porcentagem relativa
for noneto, contagem in nonetos_ordenados:
    if contagem > 1 and len(noneto) > 17:
        porcentagem = (contagem / total_contagem) * 100 if total_contagem != 0 else 0
        print(f"Noneto: {noneto}, Contagem: {contagem}, Porcentagem: {porcentagem:.2f}%")
