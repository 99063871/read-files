import time

with open("README.md") as file:
    for line in file:
        print(line)
        time.sleep(1)