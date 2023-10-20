from sys import path

path.append("..\\modulo")

from modulo import suml, prodl # importando as funções do modulo.py

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))



