d = {}

for i in range(0, 32):
    d[i] = chr(i % 32 + ord('А'))


# Индексы букв слова
def encode_val(word):
    word = word.upper()
    list_code = []
    lent = len(word)

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
                list_code.append(value)
    return list_code


# Комбинация индексов кюча и сообщения
def combine(word, key):
    idx = []
    k = 0
    for w in word:
        if k < len(key):
            idx.append([w, key[k]])
            k += 1
        else:
            k = 0
            idx.append([w, key[k]])
            k += 1
    return idx


def vig_encode(msg, key):
    text = ''
    a = encode_val(msg)
    b = encode_val(key)
    idx = combine(a, b)
    for i in idx:
        text += d[(i[0] + i[1]) % 32]
    return text


def vig_decode(msg, key):
    text = ''
    a = encode_val(msg)
    b = encode_val(key)
    idx = combine(a, b)
    for i in idx:
        text += d[(i[0] - i[1] + 32) % 32]
    return text


msg = 'Всего лишь шестьдесят строк кода получилось'
key = 'САЛЬЕРИ'
a = vig_encode(msg, key)

print(a)
print(vig_decode(a, key))
