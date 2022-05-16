import time

ReadMe = open("README.md", "r")

for line in ReadMe:
    print(line)
    time.sleep(1)