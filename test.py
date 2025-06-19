import sys
import csv

try:
    var ="deeef95"
    strCutZeroInBegin = str(hex(int(var,base=16)))[2:]
    if(len(strCutZeroInBegin)%2):
        strCutZeroInBegin="0"+strCutZeroInBegin
    string=f'{bytes.fromhex(strCutZeroInBegin)[::-1].hex()}'
    print(string)
except ValueError as e:
    print(f'{e}  {strCutZeroInBegin} ')

'''
filename=sys.argv[2]
column_to_read=int(sys.argv[1])-1


with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file))

for i in range(len(rows)):   
    
    #rows[i]+=(f"\"{bytes.fromhex(str_temp)[::-1].hex()}\"")
        
    print(len(rows[i]),rows[i],type(rows[i]),rows[i][column_to_read])

'''




    