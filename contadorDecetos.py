# Define o nome do arquivo
nome_arquivo = "estelas.txt"

# Inicializa um dicionário para armazenar a contagem de decetos
contagem_decetos = {}

# Lê o arquivo e processa cada linha
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        # Remove caracteres de quebra de linha
        linha_limpa = linha.strip()

        # Divide a linha em decetos e conta as ocorrências
        decetos = linha_limpa.split('-')
        for i in range(len(decetos) - 9):
            deceto = f"{decetos[i]}-{decetos[i+1]}-{decetos[i+2]}-{decetos[i+3]}-{decetos[i+4]}-{decetos[i+5]}-{decetos[i+6]}-{decetos[i+7]}-{decetos[i+8]}-{decetos[i+9]}"
            if len(deceto) > 19:
                contagem_decetos[deceto] = contagem_decetos.get(deceto, 0) + 1

# Ordena os decetos pela quantidade de ocorrências
decetos_ordenados = sorted(contagem_decetos.items(), key=lambda x: x[1], reverse=True)

total_contagem = sum(contagem for deceto, contagem in decetos_ordenados)

print("\nContagens de decetos de caracteres com mais do que uma ocorrência:")

# Imprime o resultado ordenado com a porcentagem relativa
for deceto, contagem in decetos_ordenados:
    if contagem > 1 and len(deceto) > 19:
        porcentagem = (contagem / total_contagem) * 100 if total_contagem != 0 else 0
        print(f"Deceto: {deceto}, Contagem: {contagem}, Porcentagem: {porcentagem:.2f}%")
