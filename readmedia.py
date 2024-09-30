import os
import time

file = open('larger.txt')
count = 0



while True:
    count += 1

    line = file.readline()
    n = 64

    fullline = tuple(line[i:i+n] for i in range(0, 1536, n))

    time.sleep(0.1)
    for i in fullline:
        print(i)

    if not line:
        break

file.close()


