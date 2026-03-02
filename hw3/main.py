import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

init(autoreset=True)

#призначення шляху до директорії
path = Path(sys.argv[1])

#створення функції яка виводе структуру директорії
def directory_structure(path, ident=0):
    #сортування назв файлів
    items = sorted(path.iterdir())
    #пройтися по всіх елементах в директорії
    for item in items:
        #якщо елемент є папкою, то початок ітерації та виведення в консоль з відступом
        if item.is_dir():
            print(" " * ident + Fore.BLUE + item.name + "/")
            directory_structure(item, ident + 4)
        #якщо елемент є файлом, то виведення назви файлу в консоль
        else:
            print(" " * ident + Fore.GREEN + item.name)

#виклик функції           
directory_structure(path)
    


