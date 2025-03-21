# Importamos la función desde listas_util.py
from listas_util import eliminar_duplicados

# Lista de ejemplo con duplicados
lista = [1, 2, 2, 3, 4, 4, 5]
# Eliminamos los duplicados
nueva_lista = eliminar_duplicados(lista)
# Imprimimos el resultado
print(nueva_lista)  # Salida: [1, 2, 3, 4, 5]