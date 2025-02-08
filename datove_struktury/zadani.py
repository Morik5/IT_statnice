from collections import Counter

# Úloha 1: Najdi nejmenší prvek v seznamu
def hledej(studenti, casy):
    return


    # Příklad
    studenti = ["Alice", "Karel", "Pavel"]
    casy = [10, 5, 7]
    hledej(studenti, casy)  # Vypíše "Karel"

#--------------------------------------------------------------
# Úloha 2: Najdi nejčastější prvek v seznamu
# Napiš funkci, která vrátí nejčastější prvek v seznamu
def nejcastejsi_prvek(seznam):
    return

# Příklad
seznam = [1, 2, 2, 3, 3, 3, 4]
print(nejcastejsi_prvek(seznam))  # Vypíše 3

#--------------------------------------------------------------
# Úloha 3: Program na FIFO frontu
# Vytvoř třídu Fronta, která bude obsahovat metody pro přidání (add), odebrání (dele) a kontrolu, zda je prázdná
class Fronta:
    def __init__(self):
        return

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
# Úloha 4: Vysvětli co dělá následující kód
class NahodnaTabulka:
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