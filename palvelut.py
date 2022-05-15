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
    self.__numero = self.luo_nro
  
  
  def luo_nro(self):
    """
    Konstruktorissa luodaan asiakasnumero käyttämällä luo_nro-metodia.
    arvotaan asiakasnumero satunnaisesti. asettaa asiakasnumero jos kutsuu
    :ivar numero: arvottu satunnainen asiakasnumero
    :type numero: int
    """
    numero = []
    numero.append(random.randint(0, 99))
    numero.append(random.randint(0, 999))
    numero.append(random.randint(0, 999))
    return numero
  
  
  def aseta_ika(self):
    """
    palauttaa ikää, muuttajana ika
    """
    return self.__ika
  
  
  def aseta_nimi(self):
    """
    palauttaa nimi, muuttajana nimi
    """
    return self.__nimi

  def aseta_numero(self):
    """
    palauttaa numeron
    """
    return f'{self.__asiakasnumero[0]:02}-{self.__asiakasnumero[1]:03}-{self.__asiakasnumero[2]:03}'

class Palvelu(Asiakas):
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
    super()
    self.tuotenimi = tuotenimi
    self.asiakkaat_lista = []

  def luo_asiakasrivi(self, asiakas):
    """
    palauttaa asiakkaan nimi, asiakasnumero ja ikän
    """
    return f"{Asiakas.aseta_nimi} ({Asiakas.aseta_numero}) on {Asiakas.aseta_ika}-vuotias."
 
  def lisaa_asiakas(self, asiakas):
    """
    laitetaan asiakkaan ikä ja nimi listaan
    append methodia käytetään listaan lisäämiseen
    """
    self.asiakkaat_lista.append(asiakas)
  
  def poista_asiakas(self, asiakas):
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
    print(f" tuotteen " + self.tuotenimi + " asiakkaat ovat: ")
    for asiakas in self.asiakkaat_lista:
      print(self.luo_asiakasrivi(asiakas))
  
class ParempiPalvelu(Palvelu):
  """
  Luokan ParempiPalvelu konstruktori saa parametrina tuotenimen,
  jonka se lähettää kantaluokan konstruktorille argumenttina.
  Konstruktorissa luodaan edut-lista ja alustetaan se tyhjäksi.
  
  eli tämä luokka käsitä tuotenimi ja tuoten edut 
  metodit:
  lisaa_edut()
  poista_edut()
  tulosta_edfut()
  """
  
  
  def __init__(self, tuotenimi):
    """
    tämä ottaa tuotenimi luokan palvelu sisältä
    :ivar _edut_: tuoten edut
    :type _edut_: list
    """
    super(ParempiPalvelu, self).__init__(tuotenimi)
    self._edut_ = []
  
  
  def lisaa_etu(self, etu):
    """
    tämä lisää edun listaan tuoten edut
    append lisää listaan _edut_
    """
    try:
      self._edut_.append(etu)
    except:
      pass
  
  
  def poista_etu(self, etu):
    """
    tämä poistaa edun listalta tuoten edut
    jos tulee virhe kun ei o poistettava se ohitetaan
    """
    try:
      self._edut_.remove(etu)
    except:
      pass
  
  
  def tulosta_edut(self):
    """
    tämä printtaa tuoten ja sen edut
    """
    print("tuotteen  " + self.tuotenimi + " edut ovat: ")
    for etu in self._edut_:
      print(etu)
