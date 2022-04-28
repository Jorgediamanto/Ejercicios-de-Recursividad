import unidecode



x = input("Introduzca la cadena que desa comprobar si es palindormo o no: ")
    
x2=x[::-1]



x3=x.replace(" ","")
x4=x2.replace(" ","")

unaccented_string1 = unidecode.unidecode(x3)
unaccented_string2 = unidecode.unidecode(x4)


skrr=True

for z in range(len(unaccented_string1)):
      if(unaccented_string1[z].lower()!=unaccented_string2[z].lower()):
        
        skrr=False


if skrr:
  print("La cadena introducida SI es un palindromo")

else:
  print("La cadena introducida NO es un palindromo")
