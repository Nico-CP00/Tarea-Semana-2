from Estudiantes import lis_est
import pandas as pd

'''
4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
'''

def recorre_notas(notas):
    asig_aprob = 0
    for n in notas:
        if n < 4.0:
            return True
    return False
        
nota_bajo_4 = 0
    
lis_est["Nota bajo 4"] = lis_est["notas"].apply(recorre_notas)

nota_bajo_4 = lis_est["Nota bajo 4"].sum()
porcentaje_bajo_4 = round((nota_bajo_4 / len(lis_est)) * 100, 2)

print("El porcentaje de estudiantes que tiene al menos una nota bajo 4.0 es de: ", porcentaje_bajo_4, "%.")