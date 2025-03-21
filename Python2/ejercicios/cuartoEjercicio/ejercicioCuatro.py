# Función para desempaquetar una tupla de tres elementos
def desempaquetar_tupla(tupla):
    a, b, c = tupla
    return a, b, c

# Tupla de ejemplo
tupla = (10, 20, 30)
# Desempaquetamos la tupla
a, b, c = desempaquetar_tupla(tupla)
# Imprimimos el resultado
print(a, b, c)  