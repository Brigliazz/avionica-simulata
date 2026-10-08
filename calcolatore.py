class Calcolatore:
    def __init__(self):
        self.risultato = 0

    def somma(self, a, b):
        self.risultato = a + b
        return self.risultato

    def sottrazione(self, a, b):
        self.risultato = a - b
        return self.risultato

    def moltiplicazione(self, a, b):
        self.risultato = a * b
        return self.risultato

    def divisione(self, a, b):
        if b != 0:
            self.risultato = a / b
            return self.risultato
        else:
            raise ValueError("Divisione per zero non consentita.")