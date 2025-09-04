from Validación import lis_est
import numpy as np

'''
5. Entrega un listado ordenado (de mayor a menor) de los estudiantes según su promedio.
'''

# Función para calcular promedio en una lista
def calc_prom(x):
    return round(np.mean(x), 1)

# Usamos el .apply para aplicar la función a toda la lista de notas
lis_est["promedio"] = lis_est["notas"].apply(calc_prom)

# Crea una lista ordenada de mayor a menor con la librería Pandas
lis_ordenada = lis_est.sort_values(by = "promedio", ascending = False)

# Para que se reinicien las IDs y así no confundir a un lector externo con los IDs iniciales de los estudiantes
lis_ordenada_sin_id = lis_ordenada.reset_index(drop = True)

print("Lista ordenada de estudiantes de mayor a menor según el promedio de los estudiantes\n", lis_ordenada_sin_id)