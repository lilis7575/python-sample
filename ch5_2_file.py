#
# file = open("dummy.txt", "w")
# file.write("this is file writing....")
# file.close()
#
# file = open("dummy.txt", "r")
# print(file.read())
# file.close()

import os

class HandleFile:
    def __init__(self, path):
        self.path = path

    def fileRead(self):
        with open(self.path, 'r') as f:
            print(f.read())

    def fileWrite(self, value):
        with open(self.path, 'w') as f:
            f.write(value)



filePath = "dummy.txt"
if os.path.exists(filePath) and os.path.isfile(filePath) :
    exist_file = True
else:
    exist_file = False

while True:
    print("Select Type <r:READ>, <w:WRITE>")
    type = input()
    if type == "r":
        print("Read File", filePath)
        f = HandleFile(filePath)
        f.fileRead()
    elif type == "w":
        print("Write File", filePath)
        value = input()
        f = HandleFile(filePath)
        f.fileWrite(value)
    elif type == "exit":
        print("Press Exit")
        break
    else:
        pass


