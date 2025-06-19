import csv
import sys

filename=sys.argv[2]
column_to_read=int(sys.argv[1])-1
row_to_start=1

#Читаем файл и записываем в rows
try:
    with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file,delimiter=';'))
except FileNotFoundError:
    print("\033[31mФайл не найден")
    sys.exit()
except PermissionError:
    print("\033[31mНет прав доступа")
    sys.exit()
except IOError as e:
    print(f"\033[31mОшибка ввода-вывода: {e}")
    sys.exit()



    
rows.append(["1;2;3"])

for i in range(row_to_start,len(rows)):
    #for j in range(len(rows[i])):
    #    if ';' in rows[i][j]:
    #        rows[i][j] = "\""+rows[i][j]+"\""
    print(len(rows[i]),rows[i])
    '''
    if(rows[i][:rows[i][0].find(';')]!=""):
        try:
            #if(len(rows[i][column_to_read])!=''):
                ind_in_str=-1
                for k in range(column_to_read):
                    ind_in_str=rows[i][0].find(';',ind_in_str+1)
                end_ind = rows[i][0].find(';',ind_in_str+1)
                str_temp = rows[i][0][ind_in_str+2:end_ind-1]


                rows[i]+=(";"+f"{bytes.fromhex(str_temp)[::-1].hex()}"+"\n")

                #rows[i].append(f"\"{bytes.fromhex(rows[i][column_to_read])[::-1].hex()}\"")
        except ValueError as e:
            print(f'puk  {e} {str_temp} {str_temp[0]}')
            sys.exit()
        except IndexError:
            print(len(rows[i]),rows[i])
    
    '''

# Перезаписываем файл
with open(filename, 'w', encoding='utf-8',newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(rows)
         
        
    










