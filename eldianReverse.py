import csv
import sys
import pytest

def ReadCSVtoRows(_filename):
     #Читаем файл и записываем в rows
    try:
        with open(_filename, 'r', encoding='utf-8') as file:
            rows = list(csv.reader(file,delimiter=delim))
            return rows
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

def TransformRows(_rows:list[list[str]],_column=0):
    #Меняем порядок байтов в rows
    for i in range(row_to_start,len(_rows)):   
        try:
            if(_rows[i][_column]!=""):                
                        strCutZeroInBegin = str(hex(int(_rows[i][_column],base=16)))[2:]
                        if(len(strCutZeroInBegin)%2):
                            strCutZeroInBegin="0"+strCutZeroInBegin
                        string=f'{bytes.fromhex(strCutZeroInBegin)[::-1].hex()}'
                        _rows[i][_column]=string
        except ValueError as e:
                print(f'puk  {e} {_rows[i][_column]} {type(_rows[i][_column])} {strCutZeroInBegin}')
                sys.exit()
        except IndexError:
                print(len(_rows[i]),_rows[i])
    return _rows

def WriteToCSV(_filename,_rows):
    # Перезаписываем файл
    with open(_filename, 'w', encoding='utf-8',newline='') as file:
        writer = csv.writer(file, delimiter=delim)
        for row in _rows:
            writer.writerow([str(cell) for cell in row])     


#Оставляем только само название файла без абсолютного пути
filename=sys.argv[1]
nameCopy = filename
ind = nameCopy.rfind('/')
if(ind!=-1):
     nameCopy=nameCopy[ind+1:]



if("aliases" in nameCopy ):
    delim=';'
    row_to_start=1
    columns=[4]
else:
    delim=","
    row_to_start=0
    columns = [0]

if(len(sys.argv)>2):
     columns = [int(x) - 1 for x in sys.argv[2:]]
     #column_to_read=int(sys.argv[2])-1
    

rows=ReadCSVtoRows(filename)
if(min(columns)<0 or max(columns)>len(rows[0])-1):
     print(f"\033[31mIncorrect column number {min(columns)-1}")
     sys.exit()
for col in columns:
    rows=TransformRows(rows,col)
WriteToCSV(filename,rows)
    
        










