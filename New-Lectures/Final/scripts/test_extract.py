import re

file_path = r'C:\Project\python-data-structures-and-algorithms\New-Lectures\Final\ข้อสอบปลายภาค_Data_Structures_Final_Exam.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

part1_start = text.find('ตอนที่ 1:')
part2_start = text.find('ตอนที่ 2:')
part3_start = text.find('ตอนที่ 3:')

print('Part 1 index:', part1_start)
print('Part 2 index:', part2_start)
print('Part 3 index:', part3_start)
