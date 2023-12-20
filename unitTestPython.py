chaine = input("Rentrez un mot : ")

reverseChaine = "".join(reversed(chaine))

if (chaine == reverseChaine):
    print(reverseChaine + "\nbien dit !")
else:
    print(reverseChaine)