from Estudiantes import estudiantes
import pandas as pd
import numpy as np

lis_est = pd.DataFrame(estudiantes)

# Verifica si hay valores nulos
lis_est.isnull().sum()

# Función que verifica si la entrada es una lista no vacía
def es_lista_no_vacia(x):
    return isinstance(x, list) and len(x) > 0
lis_est["notas"].apply(es_lista_no_vacia)

# Función para que las notas estén en el rango de 1 y 7
def limpiar_notas(notas):
    return [min(max(n, 1), 7) for n in notas]
lis_est["notas"] = lis_est["notas"].apply(limpiar_notas)

# Función que valida que todas las notas en la lista sean de tipo float
def validar_floats(notas):
    nuevos = []
    for n in notas:
        try:
            nuevos.append(float(n))
        except:
            print(f"Valor inválido encontrado: {n}")
            nuevos.append(np.nan)  #Si no es válido se elimina
    return nuevos #Regresa la lista con los datos válidos
lis_est["notas"] = lis_est["notas"].apply(validar_floats)