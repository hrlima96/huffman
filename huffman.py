import operator
from no import No

alfabeto = "abcdefghijklmnopqrstuvwxyz"

class Huffman:

    contador_letras = {letra: 0 for letra in alfabeto}
    lista = []
    lista_final = []
    lista_nos = []

    def gerar(self, texto):
    	for letra in texto:
    		if letra != " ":
    			self.contador_letras[letra] += 1

        self.lista = sorted(self.contador_letras.items(), key = operator.itemgetter(1))

        for i in range(len(self.lista)):
            if self.lista[i][1] != 0:
                self.lista_final.append(self.lista[i])

        for tupla in self.lista_final:
            self.lista_nos.append(No(tupla[0], tupla[1]))

        while len(self.lista_nos) > 1:
            s0 = self.lista_nos.pop(0)
            s1 = self.lista_nos.pop(0)
            x = No("xxx", int(s0.get_prob() + s1.get_prob()), s0, s1)
            self.lista_nos.append(x)

        x = self.lista_nos[0]
        codigos = {}

    def percorre_ate_folha(self, no):
        if no.get_filho0 == None:
            codigo = percorre_ate_folha(no.get_filho1)
        elif no.get_filho1 == None:
            codigo = percorre_ate_folha(no.get_filho0)
        else:
            







x = Huffman()
x.gerar("aaaaabbbccczzz")
