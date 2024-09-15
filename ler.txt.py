# Abrir o arquivo 'loremipsum.txt' utilizando o método 'open'
arquivo = open('loremipsum.txt', 'r')

# Ler todo o conteúdo do arquivo e imprimir na tela
conteudo = arquivo.read()
print("Conteúdo completo do arquivo:")
print(conteudo)

# Fechar o arquivo
arquivo.close()

# Reabrir o arquivo para ler novamente
arquivo = open('loremipsum.txt', 'r')

# Ler e imprimir apenas a primeira linha
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:")
print(primeira_linha)

# Fechar o arquivo novamente
arquivo.close()

# Reabrir o arquivo para ler os primeiros 3 caracteres
arquivo = open('loremipsum.txt', 'r')

# Ler e imprimir os 3 primeiros caracteres
tres_primeiros = arquivo.read(3)
print("\nOs 3 primeiros caracteres do arquivo:")
print(tres_primeiros)

# Fechar o arquivo
arquivo.close()

# Utilizando a instrução 'with' para abrir e ler o conteúdo do arquivo
with open('loremipsum.txt', 'r') as arquivo:
    conteudo_com_with = arquivo.read()

print("\nConteúdo do arquivo usando 'with':")
print(conteudo_com_with)