text = input('Enter the text: ').strip()
vowels = 'aeiouAEIOU'
a = []
for x in text:
    if x in vowels:
        a.append(x)
count = len(a)
count2 = len(text)-count
print(f'Vowels: {count}\nConsonants: {count2}')