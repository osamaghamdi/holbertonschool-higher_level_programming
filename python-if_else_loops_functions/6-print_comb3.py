#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0 and j == 1:
            print("{:02}, ".format(i * 10 + j), end="")
        else:
            print("{:02}".format(i * 10 + j), end=", " if (i < 9 or j < 9) else "")
