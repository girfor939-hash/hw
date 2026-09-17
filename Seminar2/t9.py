f = open('input.txt', 'r')
text = f.read()
f.close()

print(sum(text[i] in '.?!' and (i == 0 or text[i - 1] not in '.?!')
          for i in range(len(text))))

