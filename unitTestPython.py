import datetime
import locale

locale.setlocale(locale.LC_ALL, "")
message_language = locale.getlocale(locale.LC_CTYPE)[0]

now = datetime.datetime.now()

if (message_language == "fr_FR"):
    if (now.hour > 18):
        print("Bonsoir !")
    else:
        print("Bonjour !")
else:
    if (now.hour > 18):
        print("good evening !")
    else:
        print("Hello !")



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