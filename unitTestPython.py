import datetime

now = datetime.datetime.now()

if (now.hour > 18):
    print("Bonsoir !")
else:
    print("Bonjour !")

chaine = input("Rentrez un mot : ")

reverseChaine = "".join(reversed(chaine))


if (chaine == reverseChaine):
    print(reverseChaine + "\nbien dit !")
else:
    print(reverseChaine)

if (now.hour > 18):
    print("Bonne soirée !")
else:
    print("Bonne Journée !")