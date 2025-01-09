import json

# Carica la codifica in memoria nella variabile "codifica" come dictionary
with open("code.json", "r") as f:
    codifica = json.loads(f.read())

# Richiedi percorso del file di input
percorso=input("Inserisci il percorso del file di input: ")

# Carica il testo in una stringa
try:
    with open(percorso, "r") as f:
        testo=f.read()
except:
    raise(Exception("Sei un coglione!"))

# Sostituisce le lettere ASCII (se usi unicode puzzi) con la nostra codifica fantastica e totalmente utile
for lettera, codice in codifica.items():
    testo=testo.replace(lettera, codice)

with open(percorso+".edch", "w") as f:
    f.write(testo)