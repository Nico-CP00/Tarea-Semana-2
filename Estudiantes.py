import pandas as pd

estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 3.2, 4.8]},
    {"nombre": "Luis", "notas": [2.9, 3.1, 2.8]},
    {"nombre": "Camila", "notas": [5.5, 6.7, 4.1]},
    {"nombre": "Pedro", "notas": [3.0, 2.5, 4.0]},
    {"nombre": "Valentina", "notas": [6.9, 5.2, 3.3]},
    {"nombre": "Andrés", "notas": [2.0, 2.8, 3.1]},
    {"nombre": "Javiera", "notas": [6.3, 4.1, 6.1]},
    {"nombre": "Matías", "notas": [3.7, 2.0, 3.4]},
    {"nombre": "Francisca", "notas": [6.5, 5.8, 6.0]},
    {"nombre": "Diego", "notas": [2.5, 2.2, 3.9]},
    {"nombre": "Catalina", "notas": [4.2, 3.5, 5.8]},
    {"nombre": "Ignacio", "notas": [5.8, 4.0, 6.1]},
    {"nombre": "Fernanda", "notas": [5.9, 6.7, 2.5]},
    {"nombre": "Sebastián", "notas": [3.5, 3.9, 2.3]},
    {"nombre": "Constanza", "notas": [6.0, 2.9, 3.8]},
    {"nombre": "Felipe", "notas": [2.9, 3.6, 2.1]},
    {"nombre": "Rocío", "notas": [4.4, 2.6, 3.9]},
    {"nombre": "Tomás", "notas": [2.7, 2.9, 3.2]},
    {"nombre": "Paula", "notas": [6.8, 4.0, 4.2]},
    {"nombre": "Cristóbal", "notas": [3.1, 2.8, 2.3]},
    {"nombre": "Daniela", "notas": [5.7, 6.9, 5.0]},
    {"nombre": "Rodrigo", "notas": [4.6, 4.4, 5.8]},
    {"nombre": "María", "notas": [4.3, 3.8, 2.9]},
    {"nombre": "Nicolás", "notas": [3.9, 2.1, 3.4]},
    {"nombre": "Sofía", "notas": [6.0, 2.9, 2.0]},
    {"nombre": "Claudia", "notas": [3.0, 2.2, 4.5]},
    {"nombre": "Gabriel", "notas": [5.4, 5.8, 5.2]},
    {"nombre": "Josefa", "notas": [5.8, 3.0, 2.7]},
    {"nombre": "Mauricio", "notas": [2.6, 1.9, 2.8]},
    {"nombre": "Carolina", "notas": [4.4, 3.7, 3.8]}
]

lis_est = pd.DataFrame(estudiantes)

'''
Tarea Semana 2:
Obtener promedios de cada estudiante y promedio general del curso
1. Calcular promedio de notas de cada estudiante y determinar quién tiene el promedio más alto y el más bajo.
2. Contar cuántos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0).
3. ¿Cúal es la nota más frecuente considerando todas las notas de todos los estudiantes?
4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
5. Entrega un listado ordenado (de mayor a menor) de los estudiantes según su promedio.
'''