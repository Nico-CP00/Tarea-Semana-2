from Estudiantes import lis_est

'''
2. Contar cuántos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0).
'''

def aprobo_todo(notas):
    asig_aprob = 0
    for n in notas:
        if n >= 4.0:
            asig_aprob = asig_aprob + 1
    if asig_aprob == len(notas):
        return True
    else:
        return False

# Aplica la función para comprobar si el estudiante aprobo todo a toda la lista de estudiantes
lis_est["Aprobados"] = lis_est["notas"].apply(aprobo_todo)
total_aprob = lis_est["Aprobados"].sum()

print("Lista de estudiantes que aprobaron todas sus asignaturas\n", lis_est[["nombre", "Aprobados"]])
print("La cantidad de estudiantes aprobados fue de: ", total_aprob)