"""
nombre 
carnet 
carrera 
cui  
edad 
cursos 
------------------------------------------------------------
nombre = 'Mario Daniel Sajvin Gómez'
carnet = '1612921'
carrera = 'Ingenieria en informatica y sistemas'
cui = '3019803140101'
edad = 19
cursos =['Intro a la progra','Intro a la ingenieria', 'Calculo' ]

# Estudiante Andreé
nombre1 = 'Andree Antonio Robles Mendez'
carnet1 = '1523820'
carrera1 = 'Ingenieria en informatica y sistemas'
cui1 = '22222222'
edad1 = 19
cursos1 = ['Magis Landivariano', 'Progra avanzada', 'Quimica 1']

print(nombre)
print(carnet)

print(nombre1)
print(carnet1)
"""
estudiante1 = {
    "nombre": "Daniel Sajvin",
    "carnet": "1527521",
    "edad": 19
}

print(estudiante1)
print(estudiante1["nombre"])
print(estudiante1["carnet"])
print(estudiante1["edad"])

estudiante1["edad"] = estudiante1["edad"] - 2
print(estudiante1["edad"])

estudiante2 = {
    "nombre": "Andree Robles",
    "carnet": "8527551",
    "edad": 19
}
print(estudiante2["nombre"])
print(estudiante2["carnet"])
print(estudiante2["edad"])

listado = [
    {
    "nombre": "Daniel Sajvin",
    "carnet": "1527521",
    "edad": 19
    },
    {
    "nombre": "Andree Robles",
    "carnet": "8527551",
    "edad": 19
    }
    ]
listado.append({
    "nombre": "Fernanda Galvez",
    "carnet": "857551",
    "edad": 20
})

print (listado[0]['nombre'])
print (listado[0]['carnet'])
print (listado[0]['edad'])

print (listado[2]['nombre'])
print (listado[2]['carnet'])
print (listado[2]['edad'])