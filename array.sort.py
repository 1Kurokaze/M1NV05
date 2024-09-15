import random

# 1. Crie um array de 15 posições com números inteiros e valores aleatórios, não ordenados
array_inteiros = [random.randint(1, 100) for _ in range(15)]

# 2. Realize a ordenação dos dados do array utilizando o método “sort”
array_inteiros.sort()

# 3. Imprima, na tela, o conteúdo do array ordenado
print("Array ordenado crescente:", array_inteiros)

# 4. Utilize o método “sort” novamente, mas com parâmetros para ordenar de forma decrescente
array_inteiros.sort(reverse=True)

# 5. Imprima o array ordenado de forma decrescente
print("Array ordenado decrescente:", array_inteiros)

# 6. Crie um array de strings (nome, dataNascimento, cpf, rg)
array_strings = ["nome", "dataNascimento", "cpf", "rg"]

# 7. Ordene o array de strings de forma crescente
array_strings.sort()

# 8. Imprima o array ordenado de forma crescente
print("Array de strings ordenado crescente:", array_strings)

# 9. Ordene o array de strings de forma decrescente
array_strings.sort(reverse=True)

# 10. Imprima o array ordenado de forma decrescente
print("Array de strings ordenado decrescente:", array_strings)