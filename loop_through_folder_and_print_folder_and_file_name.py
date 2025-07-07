directory = "files/"
for filename in os.listdir(directory):
    if filename.endswith(".txt") or filename.endswith(".py"): 
        print(os.path.join(directory, filename))
        continue
    else:
        continue