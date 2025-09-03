from Estudiantes import lis_est
import pandas as pd

'''
3. ¿Cúal es la nota más frecuente considerando todas las notas de todos los estudiantes?
'''

todas_notas = []

# Como el diccionario está compuesto por más diccionarios, debemos usar ciclos for para recorrerlos y separar así todas las notas
for lista in lis_est["notas"]:
    for n in lista:
        todas_notas.append(n)
# Aquí mejor usar ".explode" en vez de usar doble ciclo for

# Usamos la librería Pandas para obtener la moda o las modas
moda = pd.Series(todas_notas).mode()

# Para ver cuantas veces se repite la nota más frecuente
notas_series = pd.Series(todas_notas)
notas_frec = notas_series.value_counts()
frecu = max(notas_frec)

print("La(s) nota(s) más frecuentes es(son): ", moda.tolist(), "y se repiten ", frecu, "veces.")