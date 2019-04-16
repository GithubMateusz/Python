import re, sys
from datetime import datetime, timedelta 
if not sys.argv[1] and  not sys.argv[2]:
    print("Nie podano nazw plików, wejściowego lub wyjściowego")
    pass
else:
    with open(sys.argv[1]) as plik:
        reg = re.compile("\s*([a-z]+[0-9]*)\s*[=]{1}\s*([a-z]+[0-9]*|[0-9]{4}[.]{1}[0-9]{2}[.]{1}[0-9]{2}|[0-9]+)\s*([+-/*])\s*([a-z]+[0-9]*|[0-9]{4}[.]{1}[0-9]{2}[.]{1}[0-9]{2}|[0-9]+)\s*")
        zmienne = {}
        nr = 0
        for wiersz in plik:
            m = reg.fullmatch(wiersz)
            nr += 1
            if m:
                zmn = m.group(1)
                arg1 = m.group(2)
                opr = m.group(3)
                arg2 = m.group(4)
                zmienne[zmn] = ""
                if arg1.isdigit() is False:
                    try:
                        arg1 = datetime.strptime(arg1,'%Y.%m.%d')
                    except ValueError:
                        if arg1 in zmienne:
                            arg1 = zmienne[arg1]
                        else:
                            print ("Błędna składnia pierwszego argumentu w lini:", nr)
                            sys.exit(1)
                else: 
                    arg1 = int(arg1)
                    
                if arg2.isdigit() is False:
                    try:
                        arg2 = datetime.strptime(arg2,'%Y.%m.%d')
                    except ValueError:
                        if arg2 in zmienne:
                            arg2 = zmienne[arg2]
                        else:
                            print ("Błędnia składnia drugiego argumentu w lini:", nr)
                            sys.exit(1)
                else:
                    arg2 = int(arg2)
                    
                if opr == '+':
                    if type(arg1) == datetime and type(arg1) != type(arg2):
                        zmienne[zmn] = arg1 + timedelta(arg2)
                    elif type(arg2) == datetime and type(arg1) != type(arg2):
                        zmienne[zmn] = timedelta(arg1) + arg2
                    elif type(arg1) == int and type(arg2) == int:
                        zmienne[zmn] = arg1 + arg2
                    else:
                        print ("Błedna operacja w lini:", nr)
                        sys.exit(1)
                elif opr == '-':
                    if type(arg1) == datetime and type(arg1) != type(arg2):
                        zmienne[zmn] = arg1 - timedelta(arg2)
                    elif  type(arg1) == datetime and type(arg2) == datetime:
                        zmienne[zmn] = (arg1 - arg2).days
                    elif  type(arg1) == int and type(arg2) == int:
                        zmienne[zmn] = arg1 - arg2
                    else:
                        print ("Błedna operacja w lini:", nr)
                        sys.exit(1)
                elif opr == '*' and type(arg1) == int and type(arg2) == int:
                    zmienne[zmn] = arg1 * arg2
                elif opr == '/' and type(arg1) == int and type(arg2) == int:
                    zmienne[zmn] = arg1 // arg2
                else:
                    print ("Błedna operacja w lini:", nr)
                    sys.exit(1)
            else:
                print ("Błedna składnia wyrażenia w lini:", nr)
                sys.exit(1)
        plik_wynikowy = open(sys.argv[2], 'w')
        for (nazwa, wartosc) in zmienne.items():
            if type(wartosc) == datetime:
                wynik = nazwa + " = " + str(wartosc.strftime("%Y.%m.%d"))
                plik_wynikowy.write(wynik)
            else:
                wynik = nazwa + " = " + str(wartosc)
                plik_wynikowy.write(wynik)
            plik_wynikowy.write(" \n")
        plik_wynikowy.close()    
            
