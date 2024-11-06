import random

# Lista di colori disponibili
colori = ["Rosso", "Blu", "Verde", "Giallo", "Nero", "Bianco"]

# Genera una sequenza segreta casuale
sequenza_segreta = [random.choice(colori) for _ in range(4)]

def valuta_tentativo(tentativo, sequenza):
    neri = sum([1 for i in range(4) if tentativo[i] == sequenza[i]])
    
    # Crea copie di tentativo e sequenza per contare i bianchi senza includere i neri
    tentativo_restante = [tentativo[i] for i in range(4) if tentativo[i] != sequenza[i]]
    sequenza_restante = [sequenza[i] for i in range(4) if tentativo[i] != sequenza[i]]
    
    # Conta i bianchi usando solo i colori restanti
    bianchi = sum([1 for c in tentativo_restante if c in sequenza_restante])
    
    # Rimuove il colore contato dalla sequenza per evitare duplicati
    for c in tentativo_restante:
        if c in sequenza_restante:
            sequenza_restante.remove(c)
    
    return neri, bianchi

print("Benvenuto a Mastermind!")
print("Devi indovinare la sequenza di 4 colori (Rosso, Blu, Verde, Giallo, Nero, Bianco)")
print("Ogni colore può comparire più volte.")

# Numero di tentativi massimo
tentativi = 10
for i in range(tentativi):
    # Legge il tentativo del giocatore
    input_tentativo = input(f"Tentativo {i + 1}/{tentativi}: Inserisci 4 colori separati da una virgola: ").split(",")
    
    # Valuta il tentativo
    neri, bianchi = valuta_tentativo(input_tentativo, sequenza_segreta)
    print(f"Pioli neri (posizione giusta e colore giusto): {neri}")
    print(f"Pioli bianchi (colore giusto, posizione sbagliata): {bianchi}")
    
    # Controlla se il giocatore ha vinto
    if neri == 4:
        print("Complimenti! Hai indovinato la sequenza!")
        print(f"La sequenza corretta era: {', '.join(sequenza_segreta)}")
        break
else:
    print("Mi dispiace, hai esaurito i tentativi.")
    print(f"La sequenza corretta era: {', '.join(sequenza_segreta)}")
