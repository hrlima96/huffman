alfabeto = "abcdefghijklmnopqrstuvwxyz"
     
class Huffman:
     
    contador_letras = {letra: 0 for letra in alfabeto}
    lista = []
     
    def gerar(self, texto):
    	for letra in texto:
    		if letra != " ":
    			self.contador_letras[letra] += 1
    			
    	while max(self.contador_letras.values()) != 0:
    		maior = max(self.contador_letras.values())
    		
    		for key in self.contador_letras.keys():
    			if self.contador_letras[key] == maior:
    				self.lista.append(key)
    				
    	print self.lista
    	print self.contador_letras
     
     
x = Huffman()
x.gerar("aaaaabbbccc")
