import time

# Função Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Função Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Função para ler o arquivo txt
def ler_arquivo(arquivo_nome):
    palavras = []
    try:
        with open(arquivo_nome, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Remover quebras de linha e separar palavras por espaços
                linha = linha.strip()
                palavras.extend(linha.split())
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_nome}' não foi encontrado.")
    return palavras

# Função para salvar palavras ordenadas no arquivo
def salvar_arquivo(arquivo_nome, palavras):
    with open(arquivo_nome, 'w', encoding='utf-8') as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + '\n')

# Lendo o conteúdo do arquivo loremipsum.txt
arquivo_txt = 'loremipsum.txt'  # Nome do arquivo de entrada
palavras = ler_arquivo(arquivo_txt)

# Verificar se há palavras no arquivo lido
if not palavras:
    print(f"O arquivo '{arquivo_txt}' está vazio ou não foi possível ler o conteúdo.")
else:
    # Ordenação com Bubble Sort
    palavras_bubble = palavras.copy()
    start_time = time.time()
    bubble_sort(palavras_bubble)
    end_time = time.time()
    print(f"Bubble Sort - Tempo de execução: {end_time - start_time:.6f} segundos")

    # Ordenação com Selection Sort
    palavras_selection = palavras.copy()
    start_time = time.time()
    selection_sort(palavras_selection)
    end_time = time.time()
    print(f"Selection Sort - Tempo de execução: {end_time - start_time:.6f} segundos")

    # Ordenação com o método nativo sort()
    palavras_sort = palavras.copy()
    start_time = time.time()
    palavras_sort.sort()
    end_time = time.time()
    print(f"Sort (Método Nativo) - Tempo de execução: {end_time - start_time:.6f} segundos")

    # Salvando as palavras ordenadas no arquivo
    arquivo_saida = 'palavras_ordenadas.txt'
    salvar_arquivo(arquivo_saida, palavras_sort)
    print(f"As palavras ordenadas foram salvas no arquivo '{arquivo_saida}'.")