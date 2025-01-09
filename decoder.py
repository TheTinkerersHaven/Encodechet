import json
import pathlib

# Carica la codifica in memoria nella variabile "codifica" come dictionary
with open("code.json", "r") as f:
    codifica = json.loads(f.read())

# Richiedi percorso del file di input
percorsoIn=input("Inserisci il percorso del file di input: ")

# Carica il testo in una stringa
try:
    with open(percorsoIn, "r") as f:
        testo=f.read()
except:
    raise(Exception("Sei un coglione!"))

# Sostituisce le lettere ASCII (se usi unicode puzzi) con la nostra codifica fantastica e totalmente utile
# for lettera, codice in codifica.items():
#     testo=testo.replace(codice, lettera)
testoOut = ""
for i in range(0, len(testo), 7):
    for lettera, codice in codifica.items():
        if codice == testo[i:i+7]:
            testoOut += lettera

percorsoOut = percorsoIn[:-5]  # Rimuove gli ultimi 4 caratteri

with open(percorsoOut, "w") as f:
    f.write(testoOut)
