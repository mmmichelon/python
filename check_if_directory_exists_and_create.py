import os

if not os.path.exists(directory):
    os.makedirs(directory)

print(os.path.isdir("/home/el"))
print(os.path.exists("/home/el/myfile.txt"))