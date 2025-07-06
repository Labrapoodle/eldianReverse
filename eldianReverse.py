import csv
import sys
import pytest


filename=sys.argv[1]
if("aliases" in filename ):
    delim=';'
    row_to_start=1
    column_to_read=4
else:
    delim=","
    row_to_start=0
    column_to_read=0
    

#Читаем файл и записываем в rows
try:
    with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file,delimiter=delim))
except FileNotFoundError:
    print("\033[31mФайл не найден")
    print(sys.argv)
    sys.exit()
except PermissionError:
    print("\033[31mНет прав доступа")
    sys.exit()
except IOError as e:
    print(f"\033[31mОшибка ввода-вывода: {e}")
    sys.exit()   


for i in range(row_to_start,len(rows)):   
    try:
        if(rows[i][column_to_read]!=""):                
                    strCutZeroInBegin = str(hex(int(rows[i][column_to_read],base=16)))[2:]
                    if(len(strCutZeroInBegin)%2):
                        strCutZeroInBegin="0"+strCutZeroInBegin
                    string=f'{bytes.fromhex(strCutZeroInBegin)[::-1].hex()}'
                    rows[i][column_to_read]=string
    except ValueError as e:
            print(f'puk  {e} {rows[i][column_to_read]} {type(rows[i][column_to_read])} {strCutZeroInBegin}')
            sys.exit()
    except IndexError:
            print(len(rows[i]),rows[i])
    
# Перезаписываем файл
with open(filename, 'w', encoding='utf-8',newline='') as file:
    writer = csv.writer(file, delimiter=delim)
    for row in rows:
        writer.writerow([str(cell) for cell in row])         
        










