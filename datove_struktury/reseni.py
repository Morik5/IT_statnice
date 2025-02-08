# Úloha 1: Najdi nejmenší prvek v seznamu
def hledej(studenti, casy):
    x = casy[0]
    y = studenti[0]
    for i in range (0, len(studenti)):
        a = len(studenti) - i - 1
        if (x > casy[a]):
            x = casy[a]
            y = studenti[a]
            
    print(y)
# Příklad
studenti = ["Alice", "Karel", "Pavel"]
casy = [10, 5, 7]
hledej(studenti, casy)  # Vypíše "Karel"

#--------------------------------------------------------------
# Úloha 2: Najdi nejčastější prvek v seznamu
# Napiš funkci, která vrátí nejčastější prvek v seznamu.
def nejcastejsi_prvek(seznam):
    pocitadlo = {}
    for prvek in seznam:
        if prvek in pocitadlo:
            pocitadlo[prvek] += 1
        else:
            pocitadlo[prvek] = 1
    
    max_pocet = max(pocitadlo.values())
    for prvek, pocet in pocitadlo.items():
        if pocet == max_pocet:
            return prvek
        
# Příklad
seznam = [1, 2, 2, 3, 3, 3, 4]
print(nejcastejsi_prvek(seznam))  # Vypíše 3

#--------------------------------------------------------------
# Úloha 3: Program na FIFO frontu
# Vytvoř třídu Fronta, která bude obsahovat metody pro přidání (add), odebrání (dele) a kontrolu, zda je prázdná
class Fronta:
    def __init__(self):
        self.polozky = []
    
    def add(self, prvek):
        self.polozky.append(prvek)
    
    def dele(self):
        if not self.je_prazdna():
            return self.polozky.pop(0)
        return None
    
    def je_prazdna(self):
        return len(self.polozky) == 0

# Příklad použití třídy Fronta
fronta = Fronta()
fronta.add(1)
fronta.add(2)
fronta.add(3)

print(fronta.dele())  # Vytiskne 1
print(fronta.dele())  # Vytiskne 2
print(fronta.je_prazdna())  # Vytiskne False
print(fronta.dele())  # Vytiskne 3
print(fronta.je_prazdna())  # Vytiskne True

#--------------------------------------------------------------
# Úloha 3: Vysvětli co dělá následující kód
class HashTabulka:
    """
    Třída HashTabulka udělá jednoduchou hashovací tabulku -> ukládá dvojice (klíč, hodnota) do tabulky
    
        __init__(velikost=10):
            Vytvoří tabulku s danou velikostí -> zatím prázdná
        _hash(klic):
            Private metoda která vrací hash hodnotu pro daný klíč. Používá součet ASCII hodnot znaků v klíči a zbytek velikost tabulky
        vloz(klic, hodnota):
            Vloží dvojici (klíč, hodnota) do hashovací tabulky. Používá hashovací funkci k určení indexu
        ziskej(klic):
            Získá hodnotu spojenou s daným klíčem. Pokud klíč neexistuje, vrátí None.
    """
    def __init__(self, velikost=10):
        self.tabulka = [[] for _ in range(velikost)]
    
    def _hash(self, klic):
        return sum(ord(znak) for znak in klic) % len(self.tabulka) # ord() vrací ascii hodnotu znaku
    
    def vloz(self, klic, hodnota):
        index = self._hash(klic)
        self.tabulka[index].append((klic, hodnota))
    
    def ziskej(self, klic):
        index = self._hash(klic)
        for ulozeny_klic, hodnota in self.tabulka[index]:
            if ulozeny_klic == klic:
                return hodnota
        return None
"""
Například pro klíč "abc":

ASCII hodnoty znaků jsou: a = 97, b = 98, c = 99
Součet těchto hodnot je 97 + 98 + 99 = 294
Pokud je délka tabulky 10, hash hodnota bude 294 % 10 = 4
Takže klíč "abc" bude uložený na indexu 4 v tabulce
"""