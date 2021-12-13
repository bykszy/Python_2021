import os.path
filepath = "D:/agh/python/jpgnapng"
files = os.listdir(filepath)
print(files)
for filename in files:
    file_ext = os.path.splitext(filename)[1]
    oldname = os.path.join(filepath, filename)
    newname = oldname.replace(file_ext, ".png")
    os.rename(oldname, newname)

files = os.listdir(filepath)
print(files)