from estudiante import Estudiante 

# Código principal 
# Instancias
gerardo = Estudiante('Gerardo', '2350421', 17)
jairo = Estudiante('Jairo', '1574220', 19)
fernanda = Estudiante('Fernanda', '1635421', 19)
daniela = Estudiante('Daniela', '1650521', 19)

print(gerardo.nombre)
print(fernanda.nombre)
print(jairo.edad)
print(daniela.edad)

#Saludar
gerardo.saludar()
fernanda.saludar()
jairo.saludar()
daniela.saludar()

# Agregar nota
gerardo.agregar_nota(65)
gerardo.agregar_nota(80)
gerardo.agregar_nota(64)
gerardo.agregar_nota(65)
print(gerardo.notas)
gerardo.mensaje_aprobado()