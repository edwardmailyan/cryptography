hard_dictionary = {"А": "11", "Б": "12", "В": "13", "Г": "14", "Д": "15", "Е": "16",
                   "Ё": "21", "Ж": "22", "З": "23", "И": "24", "Й": "25", "К": "26",
                   "Л": "31", "М": "32", "Н": "33", "О": "34", "П": "35", "Р": "36",
                   "С": "41", "Т": "42", "У": "43", "Ф": "44", "Х": "45", "Ц": "46",
                   "Ч": "51", "Ш": "52", "Щ": "53", "Ъ": "54", "Ы": "55", "Ь": "56",
                   "Э": "61", "Ю": "62", "Я": "63"}


def encoder(msg):
    msg = msg.upper()
    fraze = list(msg)
    text = ''
    for char in fraze:
        if char in hard_dictionary:
            text += hard_dictionary[char]
    return text


def decoder(key, strong=False):
    prev = 0
    text = ''
    values = list(hard_dictionary.values())
    keys = list(hard_dictionary.keys())
    if not strong:
        for i in range(2, len(key) + 2, 2):
            text += keys[values.index(key[prev:i])]
            prev += 2
    else:
        key = encoder(key)
        for i in range(2, len(key) + 2, 2):
            num = int(key[prev:i])
            if num // 10 == 1 and num % 10 < 4:
                num += 50
            elif num // 10 == 1:
                num += 40
            else:
                num -= 10
            prev += 2
            text += keys[values.index(str(num))]
    return text


def better_encoder(msg):
    msg = msg.upper()
    fraze = list(msg)
    text = ''
    for char in fraze:
        if char in hard_dictionary:
            number = int(hard_dictionary[char])
            if number // 10 == 6:
                number -= 50
            elif number // 10 == 5 and number % 10 >= 4:
                number -= 40
            else:
                number += 10
            text += str(number)
    return decoder(text)


msg = "Я устал, босс... Я очень устал."

print('КЛАССИЧЕСКИЙ КВАДРАТ ПОЛИБИУСА:')
print('-------------------------------')
print('Шифратор: ', encoder(msg))
print('Дешифратор: ', decoder(encoder(msg)))

print()

print('УЛУЧШЕННЫЙ КВАДРАТ ПОЛИБИУСА:')
print('-------------------------------')
print('Шифратор: ', better_encoder(msg))
print('Дешифратор: ', decoder(better_encoder(msg), strong=True))
