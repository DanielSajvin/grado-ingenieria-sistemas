class Nodo: 
  def __init__(self, nombre, artista):
    self.nombre = nombre 
    self.artista = artista
    self.siguiente = None
  
  def __str__(self):
      return  str(self.nombre) + str(self.artista)