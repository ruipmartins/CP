# Define o nome do arquivo
nome_arquivo = "estelas.txt"

# Inicializa um dicionário para armazenar a contagem de quatordecuplos
contagem_quatordecuplos = {}

# Lê o arquivo e processa cada linha
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        # Remove caracteres de quebra de linha
        linha_limpa = linha.strip()

        # Divide a linha em quatordecuplos e conta as ocorrências
        quatordecuplos = linha_limpa.split('-')
        for i in range(len(quatordecuplos) - 13):
            quatordecuplo = f"{quatordecuplos[i]}-{quatordecuplos[i+1]}-{quatordecuplos[i+2]}-{quatordecuplos[i+3]}-{quatordecuplos[i+4]}-{quatordecuplos[i+5]}-{quatordecuplos[i+6]}-{quatordecuplos[i+7]}-{quatordecuplos[i+8]}-{quatordecuplos[i+9]}-{quatordecuplos[i+10]}-{quatordecuplos[i+11]}-{quatordecuplos[i+12]}-{quatordecuplos[i+13]}"
            if len(quatordecuplo) > 27:
                contagem_quatordecuplos[quatordecuplo] = contagem_quatordecuplos.get(quatordecuplo, 0) + 1

# Ordena os quatordecuplos pela quantidade de ocorrências
quatordecuplos_ordenados = sorted(contagem_quatordecuplos.items(), key=lambda x: x[1], reverse=True)

total_contagem = sum(contagem for quatordecuplo, contagem in quatordecuplos_ordenados)

print("\nContagens de quatordecuplos de caracteres com mais do que uma ocorrência:")

# Imprime o resultado ordenado com a porcentagem relativa
for quatordecuplo, contagem in quatordecuplos_ordenados:
    if contagem > 1 and len(quatordecuplo) > 27:
        porcentagem = (contagem / total_contagem) * 100 if total_contagem != 0 else 0
        print(f"Quatordecuplo: {quatordecuplo}, Contagem: {contagem}, Porcentagem: {porcentagem:.2f}%")
