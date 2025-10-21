# toteutusdokumentti

## 1. yleiskuvaus
projekti on connect4 peli (6x7-ruudukolla), jossa pelaaja pelaa tekoälyä vastaan. tekoäly käyttää minimax-algortimia alpha-beta karsinnalla ja tksinkertaisella heuristiikkafunktiolla pelitilanteen arviointiin. harjoitustyössä on myös Board-luokka jolla hallitaan pelilautaa, yksikkötestejä (pytest) ja staattinen analyysi (pylint)

## 2. rakenne
- main.py: pelin pääohjelma. lukee käyttäjän syöttee ja vuorottelee pelaajan ja AI:n välillä
- src/connect4/board.py: Board-luokka (pelilauta, siirrot, kelpoisuuden tarkistus, siirtojen listaus, voittotarkistus)
- ai.py: tekoälylogiikkaa: heuristiikka (evaluate_board, evaluate_window), minimax (alpha-beta), hajautustaulu ja find_best_move
- tests/: yksikkötestit (test_board.py, test_ai.py)

## 3. tietorakenteet

### Board
- grid: 6x7-ruudukko, 0=tyhjä, 1=pelaaja, -1=tekoäly
- is_valid_move: onko sarake vapaa
- make_move: tekee pelaajan siirron sarakkeeseen, palauttaa True jos siirto onnistui, muuten False
- get_valid_moves: palauttaa listan sarakkeista, joihin voi tehdä siirron, keskisaraketta suosien
- check_winner: tarkistaa voittorivin, huomioiden vaan viimeisen siirron

### Hajautustaulu
- table: laudan staattinen esitys ja parhaan siirron arviointi viime katselulla

## 4. tekoäly ja algoritmit

### minimax+ aplha-beta
- minimax: perinteinen minimax-haku alpha-beta-karsinnalla
- Jos laudan avain löytyy hajautustaulusta, se siirto tutkitaan ensin (tehostaa karsintaa)

### iteratiivinen syventäminen
- find_best_move: suorittaa minimax-hakuja kunnes aikaraja täyttyy
- Jokaisella iteraatiolla tallennetaan paras siirto hajautustauluun

### heuristiikka
- painottaa keskisaraketta
- käy läpi kaikki 4-ruudun ikkunat eri suunnissa

## 5. testaus
- pytest-testit kattaa: 
  - Board-toiminnot: uusi lauta, lailliset siirrot, voittotarkistukset (eri suunnat)
  - AI-testit: heuristiikka suosii keskustaa (keskimmäinen sarake), minimax tunnistaa välittömät voittosiirrot

## 6. staattinen analyysi
- pylint

## 7. rajoitukset ja parannusehdotukset
- heuristiikka on aika yksinkertainen, sitä voisi laajentaa
- minimax voi olla aika hidas suurilla syvyyksillä
- find_best_move ei tällä hetkellä tarkkaile aikarajaa

## 8. tehty työ
- perustoiminnot ja minimax toteutettu
- heursitiikka on korjattu symmetriseksi (palaute labtoolin kautta)
- iteratiivinen syventäminen ja hajautustaulu!
- testit ja pylint-ajot tehty
- dokumentaatio päivitetty

## 9. liitteet
- testit: 'tests/test_board.py', 'tests/test_ai.py'
