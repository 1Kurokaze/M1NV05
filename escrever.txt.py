# Abrir (ou criar) o arquivo 'texto.txt' no modo de escrita ('w')
arquivo = open('texto.txt', 'w')

# Criar uma lista vazia
texto = list()

# Usar o método 'append' para adicionar frases à lista
texto.append("Eu sou fã de One Piece\n")
texto.append("Eu gosto muito de jogar Destiny 2\n")
texto.append("Quero acabar logo a faculdade\n")

# Escrever o conteúdo da lista no arquivo
for linha in texto:
    arquivo.write(linha)

# Fechar o arquivo após a escrita
arquivo.close()

print("Arquivo 'texto.txt' criado e preenchido com sucesso.")