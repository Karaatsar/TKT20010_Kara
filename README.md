# Connect4 (tekoälypeli)

projektissa siis toteutetaan perinteinen **connect4-peli**, jossa voi pelata 
tekoälyä vastaan.
Tekoäly hyödyntää tällä hetkellä **minimax-algoritmia** ja **alpha-beta -karsintaa**.

## Asennusohjeet

1. Asenna Poetry virallisilla ohjeilla:  
   [Poetryn asennus](https://python-poetry.org/docs/#installation)

2. Asennuksen jälkeen lisää Poetryn polku ympäristömuuttujaan (jos sitä ei vielä ole)```bash
export PATH="$HOME/.local/bin:$PATH"
3. siirry projektin hakemistoon ja asenna riippuvuudet: poetry install

## käyttöohjeet

käynnistä peli: poetry run python main.py (peliä pelataan
komentorivin kautta) (pelaaja tekee siis siirtoja valitsemalla 
sarakkeen numeron (1-7)). 

## tekoäly
tekoäly arvioi koko pelin ajan pelitilanteita heuristiikkafunktion avulla ja käyttää minimax-algoritmia alpha-beta-karsinnalla, jotta löytäisi parhaimman mahdollisen siirron

## testaus
projektissa on automaattisia yksikkötestejä, ne testaavat esimerkiksi pelilogiikkaa ja tekoälyn toimintaa. ne voidaan ajaa komennolla: 
poetry run pytest

## projektin päärakenne: 
├── ai.py                # Tekoälyn logiikka (minimax ja alpha-beta)
├── board.py             # Pelilaudan tietorakenne ja toiminnot
├── main.py              # Pääohjelma (pelin kulku)
├── tests/               # Yksikkötestit
├── README.md            # Tämä tiedosto
├── toteutusdokumentti.md
├── määrittelydokumentti.md
└── pyproject.toml





