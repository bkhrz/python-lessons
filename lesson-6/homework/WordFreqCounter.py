try:
    open('sample.txt')
except FileNotFoundError:
    print('File not found')
    text = input('Enter the text to add to the file: ')
    with open('sample.txt', 'w') as file:
        file.write(text)

with open('sample.txt') as file:
    words = file.read().lower().replace(',', '').replace('.', '')\
        .replace('?', '').replace('!','').replace('\n', ' ').split()

frequency = {}
for word in words:
    count = 0
    for x in words:
        if word==x:
            count+=1
    frequency[word] = count
print("Word count report")
print(f'Total words {len(words)}')

top_words = dict(sorted(frequency.items(), key = lambda item:item[1], reverse = True))
rank = int(input('How many top words do you want to see: '))
print(f'Top {rank} words')

i = 0
for word, count in top_words.items():
    print(f'{word} - {count}')
    i+=1
    if i == rank:
        break