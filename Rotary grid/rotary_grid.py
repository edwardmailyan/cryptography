from textwrap import wrap
import numpy as np
from itertools import chain

key = np.array([['_', 'X', '_', '_', '_', '_', '_', '_', '_', '_'],
                ['X', '_', '_', '_', 'X', '_', 'X', 'X', '_', '_'],
                ['_', 'X', '_', '_', '_', 'X', '_', '_', '_', 'X'],
                ['_', '_', '_', 'X', '_', '_', '_', 'X', '_', '_'],
                ['_', 'X', '_', '_', '_', '_', '_', '_', '_', '_'],
                ['_', '_', 'X', '_', '_', 'X', 'X', '_', '_', 'X']])

text = 'ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИ'


def encrypt(msg, key):
    word_matrix = np.copy(key)
    temp_key = np.copy(key)
    wrap_msg = wrap(msg, int(len(key[0]) * len(key) / 4))

    for i in range(4):
        idx = list(zip(*np.where(temp_key == 'X')))

        word_and_id = list(zip(wrap_msg[i], idx))

        for el in word_and_id:
            word_matrix[el[1]] = el[0]
        if i == 0:
            temp_key = np.flip(key, axis=None)
        elif i == 1:
            temp_key = np.flip(key, axis=0)
        else:
            temp_key = np.flip(key, axis=1)
    res = chain(*word_matrix)
    return ''.join(res)


def decrypt(msg, key):
    word_matrix = wrap(msg, len(key[0]))
    temp_key = np.copy(key)

    text = ''

    for i in range(4):
        idx = list(zip(*np.where(temp_key == 'X')))
        for el in idx:
            text += word_matrix[el[0]][el[1]]

        if i == 0:
            temp_key = np.flip(key, axis=None)
            print_grid(temp_key)
        elif i == 1:
            temp_key = np.flip(key, axis=0)
            print_grid(temp_key)
        else:
            temp_key = np.flip(key, axis=1)
            print_grid(temp_key)

    return text


def print_grid(key):
    for el in key:
        print(' '.join(el))
    print()


print()

msg = encrypt(text, key)

print('Исходный текст:')
print(msg)
print()
print('Процесс дешифрации и вывод сообщения:\n')
print(decrypt(msg, key))
