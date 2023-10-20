
#!/usr/bin/env python3 

" module.py - exemplo de criação de modulo " 

__counter = 0

def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum


def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod

"variavel no final do codigo para testar se o mesmo está intacto, é invisível p/ usuarios pois a variavel __main__ só" 
"retorna dentro do arquivo do modulo"

if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)
  