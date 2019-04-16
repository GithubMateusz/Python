"""Poprawny format plików csv wejściowych:
X;Y;Z;
.
.
.
liczba;liczba;liczba;

liczba ma być typu całkowitego z zakresu od -50000 do 50000"""

import sys
import glob
import csv


class DateFile:
    def __init__(self):
        self._header = None
        self._numbers = []
        self._correct_date = []

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header_value):
        self._header = header_value

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, numbers_value):
        self._numbers = numbers_value

    @property
    def correct_date(self):
        return self._correct_date

    def checkHeader(self):
        return self._header == ["X", "Y", "Z", ""] or self._header == ["X", "Y", "Z"]

    def _checkLenghtNumbers(self):
        lenght_numbers = len(self._numbers)
        if lenght_numbers == 3 or \
                (lenght_numbers == 4 and self._numbers[3] == ""):
            self.numbers = self.numbers[0:3]
            return True
        return False

    def checkNumbers(self):
        try:
            if self._checkLenghtNumbers():
                for number in self._numbers:
                    if -50000 <= int(number) <= 50000:
                        pass
                    else:
                        return False
                self._correct_date.append(self._numbers)
                return True
            else:
                return False
        except ValueError:
            return False


def normalizationNumbers(numbers):
    numbers = [
        int(number) / 50000
        if int(number) > 4
        else format(int(number) / 50000, ".5f")
        for number in numbers]
    numbers.append("")
    return numbers


def getDateFromFile(path_file):
    date_file = DateFile()
    date_error = ""

    with open(path_file, "r", newline="") as file_input:
        date_file_input = csv.reader(file_input, delimiter=";")

        for number_line, date_line in enumerate(date_file_input, 1):
            if number_line is 1:
                date_file.header = date_line
                if date_file.checkHeader() is False:
                    date_error += str(number_line) + ", "
                continue
            date_file.numbers = date_line
            correct_date = date_file.checkNumbers()
            if not correct_date:
                date_error += str(number_line) + ", "

    if date_error:
        return date_error
    return date_file


def normalizationDateInFile(path_file, date_file):
    with open(path_file, "w", newline="") as file_input:
        file = csv.writer(file_input, delimiter=";")
        file.writerow(date_file.header)
        for numbers in date_file.correct_date:
            numbers_normalization = normalizationNumbers(numbers[0:3])
            file.writerow(numbers_normalization)


def normalizationFiles(path_directory, directory_with_file):
    for path_file in directory_with_file:
        name_file = path_file.replace(path_directory, "")
        date_file = getDateFromFile(path_file)
        if type(date_file) is not str:
            normalizationDateInFile(
                path_file, date_file)
            print("Normalizacja danych w pliku:" + name_file + " przebiegła pomyślnie.")
        else:
            print("Błąd w pliku: " + name_file + " w wierszu: " + date_file[:-2])


def main():
    try:
        path_directory = sys.argv[1]
        directory_with_file = glob.glob(path_directory + "*.csv")
        if directory_with_file:
            normalizationFiles(path_directory, directory_with_file)
        else:
            sys.exit("Podano nie poprawną ścieżke do katalogu z plikami lub katalog nie zawiera plików CSV.")
    except IndexError:
        sys.exit(
            """Należy podać ścieżkę do katalogu z plikami CSV,
            możesz podać pełną ścieżkę lub jej wersje skróconą poprzedzona \".\"""")


if __name__ == "__main__":
    main()
