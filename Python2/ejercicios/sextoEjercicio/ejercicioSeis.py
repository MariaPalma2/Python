# Importamos la función desde tuplas_util.py
from tuplas_util import contar_elementos_tupla

# Tupla de ejemplo
tupla = (1, 2, 3, 1, 2, 1)
# Contamos las veces que aparece el número 1
cuenta = contar_elementos_tupla(tupla, 1)
# Imprimimos el resultado
print(cuenta) 