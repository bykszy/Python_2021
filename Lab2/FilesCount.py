import os


filepath = "../files"
count = len([file for file in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, file))])
print(count)
