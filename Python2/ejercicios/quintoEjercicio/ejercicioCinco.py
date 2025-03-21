# Importamos la función desde tuplas_util.py
from tuplas_util import crear_lista_tuplas

# Lista de ejemplo
lista = ['a', 'b', 'c', 'd']
# Creamos la lista de tuplas
lista_tuplas = crear_lista_tuplas(lista)
# Imprimimos el resultado
print(lista_tuplas)  # Salida: [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]