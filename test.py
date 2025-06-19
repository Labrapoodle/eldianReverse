import sys
import csv

var ="00000019F88FE2"
try:
    var_reverse=f'{bytes.fromhex(str(hex(int(var,base=16))[2:]))[::-1].hex()}'
    print(var_reverse)
except ValueError as v:
    print(f"kek {str(hex(int(var,base=16)))[2:]}")


'''
filename=sys.argv[2]
column_to_read=int(sys.argv[1])-1


with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file))

for i in range(len(rows)):   
    
    #rows[i]+=(f"\"{bytes.fromhex(str_temp)[::-1].hex()}\"")
        
    print(len(rows[i]),rows[i],type(rows[i]),rows[i][column_to_read])

'''




    