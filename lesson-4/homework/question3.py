txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'aeiou'
result = ''
used_letter = set()
count = 0
i = 0

while i <len(txt):
    count += 1
    result += txt[i]

    if count == 3:
        if txt[i] in vowels or txt[i] in used_letter:
            count -= 1
        else:
            if i+1 <len(txt):
                result += '_'
                used_letter.add(txt[i])
            count = 0
    i += 1
print(result)