import pytest
import os
import csv
import random

def generate_hex_numbers(count=200):
    """Генерирует 4-байтовые шестнадцатеричные числа"""
    return [format(random.getrandbits(32), '08X') for _ in range(count)]

def write_hex_to_csv(filename, hex_numbers):
    """Записывает шестнадцатеричные числа в CSV файл"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number in hex_numbers:
            writer.writerow([number])

def reverse_hex_bytes(hex_str):
    """Переворачивает байты в шестнадцатеричной строке"""
    # Разбиваем на пары байтов (2 символа) и переворачиваем порядок
    bytes_list = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
    reversed_bytes = bytes_list[::-1]
    return ''.join(reversed_bytes)

def test_eldian_reverse(tmp_path):
    # Генерируем случайные 4-байтовые шестнадцатеричные числа
    hex_numbers = generate_hex_numbers()
    
    # Создаем два CSV файла с одинаковым содержимым
    file1 = tmp_path / "keys1.csv"
    file2 = tmp_path / "keys2.csv"
    
    write_hex_to_csv(file1, hex_numbers)
    write_hex_to_csv(file2, hex_numbers)
    
    # Вызываем тестируемую программу с одним из файлов
    os.system(f"./eldianReverse.sh {file1}")
    
    # Проверяем, что файлы теперь содержат обратные байты построчно
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        
        for row1, row2 in zip(reader1, reader2):
            original_hex = row2[0].strip().upper()  # Из второго (неизмененного) файла
            reversed_hex = row1[0].strip().upper()   # Из первого (измененного) файла
            
            # Проверяем, что байты перевернуты правильно
            sTemp = str(hex(int(original_hex,base=16)))[2:]
            if(len(sTemp)%2):
                        sTemp="0"+sTemp
            expected_reversed = reverse_hex_bytes(sTemp)
            
            assert reversed_hex.lower() == expected_reversed, \
                f"Ошибка в строке: ожидалось {expected_reversed}, получено {reversed_hex}"
    

if __name__ == "__main__":
    pytest.main()