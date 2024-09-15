# Método Bubble Sort
def bubbleSort(array):
    # Laço externo para percorrer todo o array
    for i in range(len(array)):
        # Laço interno para comparar os elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Verifica se o elemento atual é maior que o próximo
            if array[j] > array[j + 1]:
                # Se for maior, troca os valores
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Array de 15 números inteiros
array = [98, 12, 56, 89, 34, 73, 62, 21, 48, 94, 3, 77, 26, 15, 67]

# Aplicando o método bubbleSort ao array
bubbleSort(array)

# Imprimindo o array ordenado
print("Array ordenado:", array)