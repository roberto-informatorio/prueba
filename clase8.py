def hola(x,y):
  print("Bienvenido",y,"tu dni es:", str(x) )

dic = {29219974:"roberto gomez",29231356:"pablo gomez",12343403:"Roberto gomez"}
print(dic)
for key in dic:
  hola(key,dic[key])