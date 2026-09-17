vowels = 'аеёиоуыэюя'

f = open('input.txt', 'r')
text = f.read()
f.close()

result = []
i = 0
while i < len(text):
    ch = text[i]
    if ch.lower() in vowels:
        j = i
        while j < len(text) and text[j].lower() in vowels:
            j += 1
        group = text[i:j]

        prev = text[i - 1] if i > 0 else ''
        if prev and prev.lower() not in vowels and prev.isalpha():
            result.append(group[0])
            result.append('с' + group[0].lower())
            result.append(group[1:])
        else:
            result.append(group)
        i = j
    else:
        result.append(ch)
        i += 1

print(''.join(result))
