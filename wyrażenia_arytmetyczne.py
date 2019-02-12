#!/usr/bin/python3
import sys

def dzialanie(arg1, arg2, arg3):
    if arg2 == "+" :
        return arg1 + arg3
    elif arg2 == "-" :
        return arg1 - arg3
    elif arg2 == "/" :
        return arg1 // arg3
    elif arg2 == "*" :
        return arg1 * arg3
    else :
        return null

def podzial(wiersz):
    wiersz = wiersz.replace("+", " + ").replace("-", " - ").replace("/", " / ").replace("*", " * ")
    arg = wiersz.split()
    try:
        suma = dzialanie(int(arg[0]), arg[1], int(arg[2]))
        if len(arg) > 3:
            return "Błędne wyrażenie"
        return suma
    except : 
        return "Błędne wyrażenie"

nazwa = sys.argv[1]
nazwa2 = sys.argv[2]
with open(nazwa) as plik:
    plik2 = open(nazwa2, "w")
    for wiersz in plik:
        suma = podzial(wiersz)
        suma = str(suma)
        plik2.write(suma)
        plik2.write("\n")
    plik2.close()
