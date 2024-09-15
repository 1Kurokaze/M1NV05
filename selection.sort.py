# Array de 15 números inteiros
array = [23, 45, 12, 78, 34, 56, 90, 67, 18, 9, 29, 100, 3, 62, 81]

# Laço externo para iterar pelos elementos do array
for i in range(len(array)):
    # A variável 'min_index' recebe o valor de 'i'
    min_index = i
    
    # Laço interno para comparar os elementos subsequentes ao atual
    for j in range(i + 1, len(array)):
        # Verifica se o valor na posição 'min_index' é maior que o valor na posição 'j'
        if array[min_index] > array[j]:
            # Se sim, atualiza 'min_index' para a posição 'j'
            min_index = j
    
    # Troca os valores: o valor na posição 'i' troca com o valor na posição 'min_index'
    array[i], array[min_index] = array[min_index], array[i]

# Imprime o array ordenado
print("Array ordenado:", array)