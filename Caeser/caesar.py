blst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
        'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


def encryptCaesar(msg, shift=3):
    ret = ""
    msg = msg.upper()
    for x in msg:
        if x in blst:
            ind = blst.index(x)
            ret += blst[(ind + shift) % 32]
        else:
            ret += x
    return ret


def decryptCaesar(msg, shift=3):
    ret = ""
    msg = msg.upper()
    for x in msg:
        if x in blst:
            ind = blst.index(x)
            ret += blst[(ind - shift + 32) % 32]
        else:
            ret += x
    return ret


def combine(word, key):
    word = word.upper()
    key = list(key)
    for i, el in enumerate(key):
        key[i] = int(el)
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


def encryptGronsfeld(word, key):
    text = ''
    comination = combine(word, key)
    for el in comination:
        text += encryptCaesar(el[0], shift=el[1])
    return text


def decryptGronsfeld(word, key):
    text = ''
    comination = combine(word, key)
    for el in comination:
        text += decryptCaesar(el[0], shift=el[1])
    return text


decrypt_msg = 'ИЦРХЭЫЩШШЩРЬЩЩМДРШУРМЮПРЭЪЩЬЭРЪРШШЩТЛЧРШКЭЗЩМЖВШЩРМЮЧЛСШЩРЬЩЩМДРШУР'
encrypt_msg = 'Пришел, увидел, победил!'
key = '4102'

for i in range(len(blst)):
    print(decryptCaesar(decrypt_msg, shift=i + 1), ' со сдвигом ', i + 1)

print()

print(encryptCaesar(encrypt_msg, shift=6))

a = encryptGronsfeld(encrypt_msg, key)

print()
print(a)
print(decryptGronsfeld(a, key))
