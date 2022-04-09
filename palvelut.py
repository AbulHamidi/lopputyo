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
    
    self.nimi_asetettu = nimi
    self.ika_asetettu = ika
    self.asiakasnumero_asetettu = numero 
  
  
  def luo_nro(self):
    """
    Konstruktorissa luodaan asiakasnumero käyttämällä luo_nro-metodia.
    arvotaan asiakasnumero satunnaisesti. asettaa asiakasnumero jos kutsuu
    :ivar numero: arvottu satunnainen asiakasnumero
    :type numero: int
    """
    eka = random.randint(0,100)
    toka = random.randint(0,100)
    kolmas = random.randint(0,1000)
    
    numero = [eka+toka+kolmas]
    return self.asiakasnumero_asetettu
  
  
  def aseta_ika(self, ika):
    """
    palauttaa ikää, muuttajana ika_asetettu
    """
    return self.ika_asetettu
  
  
  def aseta_nimi(self, nimi):
    """
    palauttaa nimi, muuttajana nimi_asetettu
    """
    return self.nimi_asetettu

  

class Palvelu:
  """
  Luokan Palvelu konstruktori saa parametrina tuotenimen. Konstruktorissa luodaan asiakkaat-lista ja alustetaan se tyhjäksi.
  mothdit:
  laita_asiakas_listaan()
  poista_asiakas_listalta()
  
  """
  def __init__(self, tuotenimi):
    """
    :ivat tuotenimi: tuotenimi
    :ivar asiakkaat_lista: lista asiakkaista, eli asiakkaiten tiedot tulee tähän
    :type tuotenimi: str
    :type asiakkaat_lista: list
    """
    self.tuotenimi = tuotenimi
    self.asiakkaat_lista = []
 
  def laita_asiakas_listaan(self, asiakas):
    """
    laitetaan asiakkaan ikä ja nimi listaan
    append methodia käytetään listaan lisäämiseen
    """
    self.asiakkaat_lista.append(asiakas)
  
  def poista_asiakas_listalta(self, asiakas):
    """
    poistaan asiakas(ika, nimi). jos asiakas ei löyty listalta, virhe ignoorataan "pass"
    """
    try:
      self.asiakkaat_lista.remove(asiakas)
      except ValueError:
        pass

  def tulosta_asiakkaat(self):
    """
    tulostaa asiakkaat
    """
    print("tuotteen " + self.tuotenimi + "asiakkaat ovat: ")
    for asiakas in self.asiakkaat_lista:
      print("  " + self.)
  
  
  def luo_asiakasrivi(self, asiakas):
    """
    tämä palauttaa asiakkaan nimi, asiakasnumero ja ikän
    """
    return f'{Asiakas.aseta_nimi(asiakas)} ({Asiakas.luo_nro(asiakas)}) on {Asiakas.aseta_ika(asiakas)}-vuotias.'
  
