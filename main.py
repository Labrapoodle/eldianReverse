import csv
import sys

filename=sys.argv[1]
column_to_read=0
row_to_start=0

#Читаем файл и записываем в rows
try:
    with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file))
except FileNotFoundError:
    print("\033[31mФайл не найден")
    sys.exit()
except PermissionError:
    print("\033[31mНет прав доступа")
    sys.exit()
except IOError as e:
    print(f"\033[31mОшибка ввода-вывода: {e}")
    sys.exit()


if(filename.startswith("aliases")):
    print("yeah, it starts")
    column_to_read=4
    
    row_to_start=1

#if(filename.startswith("dks")):
    


for i in range(row_to_start,len(rows)):
    if(len(rows[i][column_to_read])!=0):
        try:
            rows[i].append(f"\"{bytes.fromhex(rows[i][column_to_read])[::-1].hex()}\"")
        except ValueError:
            print(i,rows[i][column_to_read])
            sys.exit()

# Перезаписываем файл
with open(sys.argv[1], 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
         
        
    










