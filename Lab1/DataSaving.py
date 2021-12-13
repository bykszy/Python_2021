import os.path


filepath = "../files/testDirStruct/zamek.txt"
if os.path.exists(filepath):
    file = open(filepath, "r")
    lockcode = file.read(4)
    givencode = input("Insert a lock code to unlock it: ")
    if lockcode == givencode:
        print("Code matches")
    else:
        print("Incorrect code")

else:
    code = input('set a 4 digit code to your lock :')
    file = open(filepath, "w")
    file.write(code)
