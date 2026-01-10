from nodo import Nodo  

class Lista:
  def __init__(self):
    self.frente = None
    self.fondo = None
    self.tamanio = 0

  # Métodos para insertar
  def nuevo_insertar(self, numero):
      #nuevo = Nodo(numero)
      insertado = False
      aux = self.frente
      if self.esta_vacia():
        self.insertar_inicio(numero)
      else:  
       aux = self.frente
       while aux != None:
         
         if numero < aux.numero:
             self.insertar_antes(numero, aux.numero)
             insertado = True
         else:
             aux = aux.siguiente
       if insertado == False: 
        self.insertar_final(numero)
                  
  def insertar_inicio(self, numero):
    nuevo = Nodo(numero)
    if self.esta_vacia():
      self.frente = nuevo
      self.fondo = nuevo
    else:
      aux = self.frente
      self.frente = nuevo
      nuevo.siguiente = aux
    self.tamanio += 1

  def insertar_final(self, numero):
    nuevo = Nodo(numero)
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

  def insertar_antes(self, numero, referencia):
    nuevo = Nodo(numero)

    # Posicionar aux con el valor de la referencia 
    aux = self.buscar_nodo_valor(referencia)

    if aux.numero == self.frente.numero:
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

  def insertar_despues(self, numero, referencia):
    nuevo = Nodo(numero)
    aux = self.buscar_nodo_valor(referencia)
    
    if aux.numero == self.fondo.numero:
      #nuevo.siguiente = aux
      #self.fondo = nuevo
      self.insertar_final(numero)
    else:
      posicion = self.buscar_posicion_nodo(referencia)
      despues = self.buscar_nodo_posicion(posicion + 1)

      # Enlazar los nodos
      aux.siguiente = nuevo
      nuevo.siguiente = despues
      #posicion = self.buscar_posicion_nodo(referencia)
      #despues = self.buscar_nodo_posicion(posicion + 1)
      #despues.siguiente = nuevo
      #nuevo.siguiente = aux

  # Métodos para buscar
  def buscar_nodo_valor(self, valor):
    aux = self.frente
    while aux != None:
      if valor == aux.numero:
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

  def buscar_posicion_nodo(self, referencia):
    aux = self.frente
    iteraciones = 0
    while aux != None:
      # ¿Es {aux.nombre} igual a {referencia}?
      if aux.numero == referencia:
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