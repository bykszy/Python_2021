file_path = "../files/test.txt"
words_to_remove = ["sie", "i", "oraz", "nigdy", "dlaczego"]


with open(file_path, 'r') as in_file:
    text_input = in_file.read()

print("before: ")
print(text_input)
words_input = text_input.split()
new_words = [word for word in words_input if word not in words_to_remove]
new_text = " ".join(new_words)
print("after: ")
print(new_text)
