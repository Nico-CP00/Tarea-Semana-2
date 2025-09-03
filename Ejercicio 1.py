from Estudiantes import estudiantes
import pandas as pd

'''
1. Calcular promedio de notas de cada estudiante y determinar quién tiene el promedio más alto y el más bajo.
Calcular promedio general del curso.
'''

lis_est = pd.DataFrame(estudiantes)

# Función para calcular promedio en una lista
def calc_prom(x):
    prom = sum(x) / len(x)
    return round(prom, 1)

# Usamos el .apply para aplicar la función a toda la lista de notas
lis_est["promedio"] = lis_est["notas"].apply(calc_prom)

mej_prom = max(lis_est["promedio"])
peor_prom = min(lis_est["promedio"])

# Con .loc ubica la columna que corresponda a los promedios correspondientes, se agrega el values[0] para obtener solo el string "nombre"
mej_nom = lis_est.loc[lis_est["promedio"] == mej_prom, "nombre"].values[0]
peor_nom = lis_est.loc[lis_est["promedio"] == peor_prom, "nombre"].values[0]

prom_gen = calc_prom(lis_est["promedio"])

print("Lista de promedios de los estudiantes\n", lis_est[["nombre", "promedio"]])
print("El mejor promedio fue de: ", mej_prom, ", correspondiente a: ", mej_nom)
print("El peor promedio fue de: ", peor_prom, ", correspondiente a: ", peor_nom)
print("El promedio general del curso fue de: ", prom_gen)