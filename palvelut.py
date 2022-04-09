import random

class Asiakas:
  
  """
  Luokan Asiakas konstruktori saa parametreina nimen ja iän. Konstruktorissa luodaan asiakasnumero käyttämällä luo_nro-metodia.
  nämä toiminnot laittaa asiakkaalle nimi, ikä ja numero.
  """
  
  def __init__(self, nimi, ika):
    
    """
    tässä on muuttujat:
    :ivar nimi: asiakas
    :ivar ika: asiakkaan ika
    :ivar numero: asiakasnumero joka arvotaan satunnaisesti
    :type nimi: str
    :type ika : int
    :type numero: int
    """
    
    self.__nimi = nimi
    self.__ika = ika
    self.__numero = luo_nro()
    
  def luo_nro(self):
    """
    Konstruktorissa luodaan asiakasnumero käyttämällä luo_nro-metodia.
    arvotaan asiakasnumero satunnaisesti
    :ivar numero: arvottu satunnainen asiakasnumero
    :type numero: int
    """
    eka = random.randint(0,100)
    toka = random.randint(0,100)
    kolmas = random.randint(0,9)
    
    numero = [eka+toka+kolmas]
    return numero
  
  
