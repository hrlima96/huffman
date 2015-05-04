import operator

alfabeto = "abcdefghijklmnopqrstuvwxyz"
     
class Huffman:
     
    contador_letras = {letra: 0 for letra in alfabeto}
    lista = []
     
    def gerar(self, texto):
    	for letra in texto:
    		if letra != " ":
    			self.contador_letras[letra] += 1
    
        self.lista = sorted(self.contador_letras.items(), key = operator.itemgetter(1))
        
    	
        print self.contador_letras
    	print self.lista

     
     
x = Huffman()
x.gerar("aaaaabbbccczzz")
