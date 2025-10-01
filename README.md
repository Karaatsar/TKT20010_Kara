# Projekti

projektissa siis toteutetaan perinteinen connect4-peli, jossa voi pelata 
tekoälyä vastaan.
Tekoäly hyödyntää tällä hetkellä minimax-algoritmia ja alpha-beta 
karsintaa.
## Asennusohjeet

1. Asenna Poetry virallisilla ohjeilla:  
   [Poetryn asennus](https://python-poetry.org/docs/#installation)

2. Asennuksen jälkeen lisää Poetryn binäärin polku `PATH`-muuttujaan.  
   Lisää kotihakemiston `.bashrc`-tiedoston loppuun rivi:

   ```bash
   export PATH="$HOME/.local/bin:$PATH

## käyttöohjeet

1. käynnistä peli: poetry run python main.py (peliä pelataan
komentorivin kautta) (pelaaja tekee siis siirtoja valitsemalla 
sarakkeen numeron (0-6)). 



