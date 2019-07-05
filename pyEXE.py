# pyEXE v0.1.3
# Експорт .py в .exe

import subprocess as sp
import time

pi = "pyinstaller"


# таймер
def countdown():
    time.sleep(1)
    print("\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("\n- - - СТАРТ - - -")


# корень
print("\n- - - Запуск pyEXE - - -\n\nПроверка наличия pyinstaller...")
sp.call('pip install ' + pi)
print("- - - Готово - - -\n")

print("\nВведите название файла '.py': ")
namepy = input()
if namepy[-3:] != ".py":
    namepy = namepy + ".py"

print("Скрыть консоль? (y / n): ")
ww = input()
if ww == "y":
    ww = "-w "
else:
    ww = ""

print("Упаковать в один файл? (y / n): ")
FF = input()
if FF == "y":
    FF = "-F "
else:
    FF = ""

print("Изменить стандартную иконку? (y / n): ")
ii = input()
if ii == "y":
    ii = "-i "
    print("Введите название иконки '.ico': ")
    nameico = input()
    if nameico[-4:] != ".ico":
        nameico = nameico + ".ico "
    else:
        nameico = nameico + " "
else:
    ii = ""
    nameico = ""

countdown()
sp.call(pi + ' ' + ww + FF + ii + nameico + namepy)
print("- - - ФИНИШ - - -\n")
print("Нажмите ENTER для выхода!")
finish = input()

# "-w" - GUI приложение / "-F" - упакованое приложение в один файл / "-i" - изменить стандартную иконку на свою
