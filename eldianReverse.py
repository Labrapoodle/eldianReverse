import csv
import sys

filename=sys.argv[2]
column_to_read=int(sys.argv[1])-1
row_to_start=0

if(column_to_read==4):
    delim=';'
    row_to_start=1
else:
    delim=","

#Читаем файл и записываем в rows
try:
    with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file,delimiter=delim))
except FileNotFoundError:
    print("\033[31mФайл не найден")
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
                #if(len(rows[i][column_to_read])!=''):
                #    ind_in_str=-1
                #    for k in range(column_to_read):
                #        ind_in_str=rows[i][0].find(';',ind_in_str+1)
                #    end_ind = rows[i][0].find(';',ind_in_str+1)
                #    str_temp = rows[i][0][ind_in_str+2:end_ind-1]
                    strCutZeroInBegin = str(hex(int(rows[i][column_to_read],base=16)))[2:]
                    if(len(strCutZeroInBegin)%2):
                        strCutZeroInBegin="0"+strCutZeroInBegin
                    string=f'{bytes.fromhex(strCutZeroInBegin)[::-1].hex()}'
                    rows[i][column_to_read]='\t'+string

                    #rows[i].append(f"\"{bytes.fromhex(rows[i][column_to_read])[::-1].hex()}\"")
    except ValueError as e:
            print(f'puk  {e} {rows[i][column_to_read]} {type(rows[i][column_to_read])} {strCutZeroInBegin}')
            sys.exit()
    except IndexError:
            print(len(rows[i]),rows[i])
    

print(rows)
# Перезаписываем файл
with open(filename, 'w', encoding='utf-8',newline='') as file:
    writer = csv.writer(file, delimiter=delim)
    #writer.writerows(rows)
    for row in rows:
        writer.writerow([str(cell) for cell in row])         
        
    










