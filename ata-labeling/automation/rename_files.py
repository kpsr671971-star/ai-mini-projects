import os

files = os.listdir()
for index, file in enumerate(files):
    os.rename(file, f"file_{index}.txt")
