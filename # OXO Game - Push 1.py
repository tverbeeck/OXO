# OXO Game - Push 1

# Initiëel spelbord mbv een dictionary
spelbord = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

def toon_spelbord():
    """Toont het spelbord in een leesbaar formaat."""
    print(f"{spelbord[7]}|{spelbord[8]}|{spelbord[9]}")
    print("-+-+-")
    print(f"{spelbord[4]}|{spelbord[5]}|{spelbord[6]}")
    print("-+-+-")
    print(f"{spelbord[1]}|{spelbord[2]}|{spelbord[3]}")


# Initiële oproep van de methode om het lege bord te tonen
toon_spelbord()
