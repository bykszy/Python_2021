path = "../files/test.txt"
replace = {
    'i': 'oraz',
    'oraz': 'i',
    'nigdy': 'prawie nigdy',
    'dlaczego': 'czemu'
}


with open(path, 'r') as file:
    text_input = file.read()
    
print("before: ")
print(text_input)

new_words = []
for word in text_input.split():
    if word in replace.keys():
        new_words.append(replace[word])
    else:
        new_words.append(word)

new_text = " ".join(new_words)
print("after: ")
print(new_text)
