# -*- coding: utf-8 -*-
import sys

def search_transcript():
    sys.stdout.reconfigure(encoding='utf-8')
    p = r'C:\Project\voice-text\03_Data_Structures_and_Algorithms\20261007_092525.txt'
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()

    print("Transcript Length:", len(text))
    print("=== LAST 3000 CHARACTERS OF TRANSCRIPT ===")
    print(text[-3000:])

if __name__ == '__main__':
    search_transcript()
