from textwrap import wrap

fraze = 'ВЩИТЗЬВЬЛОНЕНИУШИЗЕГАЕТСЮЕНОЙОСВЕПТПЫВЗШТРРОБОПАЕАОМНЛОЛОТМРЯЯЕЬЛОЛЕНА'

arr = []
for i in range(5, round(len(fraze)/2)):
    arr.append(wrap(fraze, i))

for el in arr:
    text = ''
    for i in range(max(map(len, el))):
        for word in el:
            if i < len(word):
                text += word[i]
    if len(fraze) == len(text):
        print(text)