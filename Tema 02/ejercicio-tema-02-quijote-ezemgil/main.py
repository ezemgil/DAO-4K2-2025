# Quijote
# 89765 | Gil Matías
import string

# 1. Cantidad de palabras únicas (sin repetición) del libro.
archivo = open('quijote.txt')
todo = archivo.read()
palabras = todo.split()
novela = set(p.strip(string.punctuation) for p in palabras)
print(len(novela))

# 2. Canitdad de palabras del diccionario.
diccionario = open('words_alpha.txt')
dicc = set(diccionario.read().split())
print(len(dicc))

# 3. Cantidad de palabras que no existen en el diccionario.
inexistentes = novela - dicc
print(len(inexistentes)) # 20554

# 4. Listado ordenados de todas las palabras que no existen
print(sorted(inexistentes))