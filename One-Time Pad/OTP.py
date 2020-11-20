from random import randint

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж',
            'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
            'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
            'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю',
            'Я', '0', '1', '2', '3', '4', '5', '6',
            '7', '8', '9', '.', ',', '!', '?', ' ']

text = 'Место встречи изменить нельзя'

key = str(randint(2, 10**len(text)))


# Комбинация индексов кюча и сообщения
def combine(msg, key):
    idx = []
    k = 0
    for char in msg:
        if k < len(key):
            idx.append([char, int(key[k])])
            k += 1
        else:
            k = 0
            idx.append([char, int(key[k])])
            k += 1
    return idx


def code_to_text(code):
    text = ''
    for char in code:
        text += alphabet[int(char)]
    return text


def encode(msg, key):
    msg = msg.upper()
    letter_key = combine(msg, key)

    encoded = []
    for letter, num in letter_key:
        encoded.append((alphabet.index(letter) + 1 + num) % len(alphabet))
    return code_to_text(encoded)


def decode(msg, key):
    msg = msg.upper()
    letter_key = combine(msg, key)

    decoded = []
    for letter, num in letter_key:
        decoded.append((alphabet.index(letter) - 1 - num) % len(alphabet))
    return code_to_text(decoded)


a = encode(text, key)


print('------------------------------------------')
print('Полученное сообщение в зашифрованном виде:')
print(a)
print('------------------------------------------')
print('Одноразовый ключ:')
print(key)
print('------------------------------------------')
print('Расшифрованное сообщение:')
print(decode(a, key))

print()
print()
print('------------------------------------------')
print('Сообщение для напарника:')
text = 'Москва слезам не верит'
print(text)
print('------------------------------------------')
print('Одноразовый ключ:')
key = str(randint(2, 10**len(text)))
print(key)
print('------------------------------------------')
print('Зашифрованное сообщение:')
print(encode(text, key))