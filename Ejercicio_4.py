from Validación import lis_est
import numpy as np

'''
4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
'''

# Función que verifica si en las notas hay alguna que sea menor a 4
def tiene_bajo_4(notas):
    return (np.array(notas) < 4.0).any()
    
# Aplica la función a toda la lista de estudiantes
lis_est["Nota bajo 4"] = lis_est["notas"].apply(tiene_bajo_4)

nota_bajo_4 = lis_est["Nota bajo 4"].sum()
porcentaje_bajo_4 = round((nota_bajo_4 / len(lis_est)) * 100, 2)

print("El porcentaje de estudiantes que tiene al menos una nota bajo 4.0 es de: ", porcentaje_bajo_4, "%.")