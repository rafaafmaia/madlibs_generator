with open("story.txt", "r") as f: # Abrindo o arquivo 'story.txt' para leitura
    story = f.read() # Lê o conteúdo do arquivo e armazena na variável 'story'

words = set() # Cria um conjunto vazio para armazenar as palavras encontradas
start_of_word = -1 # Inicializa a variável que indica a posição do início de uma palavra

target_start = "<" # Define os delimitadores de início e fim da palavra a ser substituída
target_end = ">"

for i, char in enumerate(story): # Itera sobre cada caractere da história para identificar as palavras entre < e >
    if char == target_start: # Verifica se o caractere é o início de uma palavra
        start_of_word = i # Marca o início da palavra

    if char == target_end and start_of_word != -1: # Verifica se o caractere é o fim da palavra
        word = story[start_of_word: i + 1] # Extrai a palavra delimitada por < e >
        words.add(word) # Adiciona a palavra ao conjunto de palavras
        start_of_word = -1 # Reseta a variável de início de palavra

answers = {} # Cria um dicionário vazio para armazenar as substituições de palavras

for word in words: # Solicita ao usuário que forneça palavras para substituir as encontradas no texto
    answer = input("Enter a word for " + word + ": ") # Pede ao usuário para digitar uma palavra para substituir a encontrada no texto
    answers[word] = answer # Armazena a palavra fornecida no dicionário de respostas

for word in words: # Substitui cada ocorrência das palavras encontradas pela palavra fornecida pelo usuário
    story = story.replace(word, answers[word])

print(story) # Exibe a história modificada com as substituições