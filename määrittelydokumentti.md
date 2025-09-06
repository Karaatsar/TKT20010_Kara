# Määrittelydokumentti
**Opinto-ohjelma:**  
tietojenkäsittelytieteen kandidaatti (TKT)  

**Dokumentaation kieli:**  
suomi

---

## Käytettävät kielet
- Pääohjelmointikieli: Python  
- Muut kielet, joita hallitsen vertaisarviointia varten: R ja SQL

---

## Algoritmit ja tietorakenteet
- Toteutettavat algoritmit: minimax (ehkä negamax) alpha-beta karsinnalla
- Toteutettavat tietorakenteet: pelilauta (6x7 ruudukko), pelipuu tekoälylle

---

## Ratkaistava ongelma
Connect4! Varsinkin minimax-algoritmin tehostaminen. 

---

## Syötteet ja niiden käyttö
- Ohjelma saa syötteenä käyttäjän valitseman sarakkeen (1-7). se toimii niin että, 
nappula lisätään valittuun sarakkeeseen pelitilanne päivitetään ja sitten katsotaan 
voittiko pelaaja. Mahdollisista virheistä (sarake tai rivi on täynnä ilmoitetaan
virheilmoituksella. 

---

## Aika- ja tilavaativuus
- Algoritmien aikavaativuus (O-analyysi): O(1)   
- Tilavaativuus: O(1)
- Perustelu, miksi nämä vaativuudet pätevät: Pelilauta on kiinteä (6x7=42 ruutua)
  Peruspelitilanne on tehdä siirto ja tarkistaa tuliko voitto, joten se on hyvin
  kevyt, eli siinä on vakio-aika ja tilavuus. Tekoäly tulee lisäämään aikavaativuutta
  kuten myös tilavaativuutta. 

---

## Lähteet
- https://en.wikipedia.org/wiki/Connect_Four
- ja myös jotain muuta, en ole vielä katsonut tarkasti läpi. 

---

## Harjoitustyön ydin
yksinkertaisesti, työn ydin on tekoäly ja sen tehostaminen. 
