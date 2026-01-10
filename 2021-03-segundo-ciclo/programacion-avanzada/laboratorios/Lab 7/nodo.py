class Nodo: 
  def __init__(self, numero):
    self.numero = numero 
    self.siguiente = None
  
  def __str__(self):
      return str(self.numero)