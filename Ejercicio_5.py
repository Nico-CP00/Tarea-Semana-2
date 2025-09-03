from Estudiantes import lis_est

'''
5. Entrega un listado ordenado (de mayor a menor) de los estudiantes según su promedio.
'''

# Función para calcular promedio en una lista
def calc_prom(x):
    prom = sum(x) / len(x)
    return round(prom, 1)

# Usamos el .apply para aplicar la función a toda la lista de notas
lis_est["promedio"] = lis_est["notas"].apply(calc_prom)

# Crea una lista ordenada de mayor a menor con la librería Pandas
lis_ordenada = lis_est.sort_values(by = "promedio", ascending = False)

print("Lista ordenada de estudiantes de mayor a menor según el promedio de los estudiantes\n", lis_ordenada)