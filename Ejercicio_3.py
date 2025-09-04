from Validación import lis_est
import pandas as pd

'''
3. ¿Cúal es la nota más frecuente considerando todas las notas de todos los estudiantes?
'''

todas_notas = []

todas_notas = lis_est.explode("notas")["notas"]

# Usamos la librería Pandas para obtener la moda o las modas
moda = (todas_notas).mode()

# Para ver cuantas veces se repite la nota más frecuente
notas_series = pd.Series(todas_notas)
notas_frec = notas_series.value_counts()
frecu = max(notas_frec)

print("La(s) nota(s) más frecuentes es(son): ", moda.tolist(), "y se repiten ", frecu, "veces.")