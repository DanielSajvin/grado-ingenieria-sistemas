from nodo import Nodo  

class Lista:
  def __init__(self):
    self.frente = None
    self.fondo = None
    self.tamanio = 0

  # Métodos para insertar
  def insertar_inicio(self, nombre):
    nuevo = Nodo(nombre)
    if self.esta_vacia():
      self.frente = nuevo
      self.fondo = nuevo
    else:
      aux = self.frente
      self.frente = nuevo
      nuevo.siguiente = aux
    self.tamanio += 1

  def insertar_final(self, nombre, artista):
    nuevo = Nodo(nombre, artista)
    aux = self.fondo
    if self.esta_vacia():
      self.frente = nuevo
      self.fondo = nuevo
    else:
      aux = self.fondo
      self.fondo = nuevo
      aux.siguiente = nuevo
      #Otra solución:
      #self.fondo.siguiente = nuevo
      #self.fondo = nuevo
    self.tamanio += 1

  def insertar_antes(self, nombre, referencia):
    nuevo = Nodo(nombre)

    # Posicionar aux con el valor de la referencia 
    aux = self.buscar_nodo_valor(referencia)

    if aux.nombre == self.frente.nombre:
      nuevo.siguiente = aux
      self.frente = nuevo
      # Otra solución:
      # self.insertar_inicio(nombre)
    else:
      # Posicionar el puntero anterior
      # Obtener la posición de la referencia (1)
      posicion = self.buscar_posicion_nodo(referencia)
      anterior = self.buscar_nodo_posicion(posicion - 1)

      # Enlazar los nodos
      anterior.siguiente = nuevo
      nuevo.siguiente = aux

  def insertar_despues(self, nombre, referencia):
    nuevo = Nodo(nombre)
    aux = self.buscar_nodo_valor(referencia)
    
    if aux.nombre == self.fondo.nombre:
      #nuevo.siguiente = aux
      #self.fondo = nuevo
      self.insertar_final(nombre)
      self.tamanio += 1
    else:
      posicion = self.buscar_posicion_nodo(referencia)
      despues = self.buscar_nodo_posicion(posicion + 1)

      # Enlazar los nodos
      aux.siguiente = nuevo
      nuevo.siguiente = despues
      self.tamanio += 1
      #posicion = self.buscar_posicion_nodo(referencia)
      #despues = self.buscar_nodo_posicion(posicion + 1)
      #despues.siguiente = nuevo
      #nuevo.siguiente = aux

  # Métodos para eliminar
  def eliminar_inicio(self):
    if self.esta_vacia() == True:
      raise Exception('Subdesbordamiento de lista')
    elif self.frente == self.fondo:
      aux = self.frente
      self.frente = None
      self.fondo = None
      self.tamanio -= 1
      return aux
    else:
      aux = self.frente
      #self.frente = self.frente.siguiente
      self.frente = aux.siguiente
      aux.siguiente = None
      self.tamanio -= 1
      return aux

  def mover_adelante(self):
      aux1 = self.frente
      aux2 = self.fondo
      self.frente = aux1.siguiente
      aux2.siguiente = aux1
      self.fondo = aux1
      aux1.siguiente = None
    
  def mover_atras(self, artista):
      aux1 = self.frente
      aux2 = self.fondo
      posicion = self.buscar_posicion_nodo(aux2.nombre, aux2.artista)
      antes = self.buscar_nodo_posicion(posicion - 1)
      antes.siguiente = None
      self.frente.siguiente = aux2
      self.frente = self.fondo
      self.fondo = antes

  def eliminar_final(self):
    if self.esta_vacia() == True:
      raise Exception('Subdesbordamiento de lista')
    elif self.frente == self.fondo:
      aux = self.frente
      self.frente = None
      self.fondo = None
      self.tamanio -= 1
      return aux
    else:
      aux = self.fondo
      posicion = self.buscar_posicion_nodo(aux.nombre, aux.artista)
      anterior = self.buscar_nodo_posicion(posicion - 1)
      self.fondo = anterior
      anterior.siguiente = None
      # Self.fondo.siguiente = None
      self.tamanio -= 1
      return aux

  def eliminar_referencia(self, referencia, artista):
    # 1. La referencia no existe
    aux = self.buscar_nodo_valor(referencia, artista)
    # 2. Solo hay un elemento en la lista
    # 3. La referencia está en el frente
    if self.frente == aux:
      return self.eliminar_inicio()
      # 4. La referencia es el fondo
    elif self.fondo == aux:
      return self.eliminar_final()
      # 5. La referencia está en otra posición
    else: 
      posicion = self.buscar_posicion_nodo(referencia, artista)
      anterior = self.buscar_nodo_posicion(posicion - 1)
      posterior = self.buscar_nodo_posicion(posicion + 1)
      anterior.siguiente = posterior
      aux.siguiente = None
      self.tamanio -= 1
      return aux

  # Métodos para buscar
  def buscar_nodo_valor(self, valor, artista):
    aux = self.frente
    while aux != None:
      if valor == aux.nombre and artista == aux.artista:
        return aux
      else:
        aux = aux.siguiente
    raise Exception('El elemento no existe')

  def buscar_nodo_posicion(self, posicion):
    iteraciones = 0
    aux = self.frente
    while aux != None:
      # ¿Es {posicion} igual a {iteraciones}?
      if posicion == iteraciones:
        return aux
      else:
        iteraciones += 1
        aux = aux.siguiente
    raise Exception('Posición no existe')

  def buscar_posicion_nodo(self, referencia, artista):
    aux = self.frente
    iteraciones = 0
    while aux != None:
      # ¿Es {aux.nombre} igual a {referencia}?
      if aux.nombre == referencia and aux.artista == artista:
        return iteraciones
      else:
        aux = aux.siguiente
        iteraciones += 1
    raise Exception('La referencia no existe')

  # Métodos auxiliares

  def esta_vacia(self):
    return self.frente == None and self.fondo == None
  
  def recorrer(self):
    resultado = ''
    aux = self.frente
    while aux != None:
      if aux == self.fondo:
        resultado += str(aux)
      else:
        resultado += str(aux) + ' -> '
      aux = aux.siguiente
    
    return resultado

  def __str__(self):
    resultado = 'Estado de la cola:\n'
    resultado += f"Tamaño: {self.tamanio}\n"
    resultado += f"Frente: {self.frente}\n"
    resultado += f"Fondo: {self.fondo}\n"
    return resultado