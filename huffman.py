import operator

alfabeto = "abcdefghijklmnopqrstuvwxyz"
     
class Huffman:
     
    contador_letras = {letra: 0 for letra in alfabeto}
    lista = []
    lista_final = []
     
    def gerar(self, texto):
    	for letra in texto:
    		if letra != " ":
    			self.contador_letras[letra] += 1
    
        self.lista = sorted(self.contador_letras.items(), key = operator.itemgetter(1))
        
        for i in range(len(self.lista)):
            if self.lista[i][1] != 0:
                self.lista_final.append(self.lista[i])

        while len(self.lista_final) > 1:
            s0 = min(self.lista_final)
            self.lista_final.pop(self.lista_final.index(min(self.lista_final)))
            s1 = min(self.lista_final)
            self.lista_final.pop(self.lista_final.index(min(self.lista_final)))
            print self.lista_final


     
     
x = Huffman()
x.gerar("aaaaabbbccczzz")
