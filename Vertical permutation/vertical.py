from itertools import permutations
import numpy as np
import textwrap

word = 'ФТБЕОЗРЬЩМАОСЕОИАОИНШВОНЖ'
key = 'XX5X1'

arr = textwrap.wrap(word, round(len(word) / 5))  # разделение текста на слова
key = list(key)

for i, k in enumerate(key):
    if k != 'X':
        key[i] = int(k) - 1

lost_keys = []
for i in range(len(key)):
    if i not in key:
        lost_keys.append(i)

# Все варианты комбинации потеряных ключей
lost_keys = list(permutations(lost_keys, 3))

# Все варианты комбинации всех ключей
key_vars = []
for el in lost_keys:
    k = key.copy()
    for i in range(3):
        k[k.index('X')] = el[i]
    key_vars.append(k)

# Вариации комбинации слов
variations = []
for variation in key_vars:
    text = []
    for i in variation:
        text.append(arr[i])
    variations.append(text)

# Вывод получившегося текста
text = []
for var in variations:
    for i, word in enumerate(var):
        var[i] = list(word)
    var = np.array(var).T
    var = np.concatenate(var)
    print(''.join(var))
