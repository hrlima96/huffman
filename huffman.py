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

        while len(self.lista_final) > 2:
            s0 = self.lista_final.pop(0)
            s1 = self.lista_final.pop(1)
            x = No(s0[1] + s1[1])
            x.set_filho0(s0)
            x.set_filho1(s1)
            print x

     
     
x = Huffman()
x.gerar("aaaaabbbccczzz")
