class No:
    letra = ""
    prob = 0
    filho0 = None
    filho1 = None

    def __init__(self, letra, prob, filho0=None, filho1=None):
        self.letra = letra
        self.prob = prob
        self.filho0 = filho0
        self.filho1 = filho1

    def __str__(self):
        return "Letra: " + str(self.letra) + ", Prob: " + str(self.prob) + ", Filho 0: " + str(self.filho0) + ", Filho 1: " + str(self.filho1)

    def get_prob(self):
        return int(self.prob)

    def get_filho0(self):
        return self.filho0

    def get_filho1(self):
        return self.filho1
