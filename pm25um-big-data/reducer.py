#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    
    # Parse input dari mapper
    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        # Jika baris tidak memiliki tab atau count bukan angka, lewati
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f'{current_word}\t{current_count}')
        current_word = word
        current_count = count

if current_word == word:
    print(f'{current_word}\t{current_count}')