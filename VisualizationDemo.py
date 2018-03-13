import matplotlib.pyplot as plt
import numpy as np
import sys

count = 0
xbuff = []
ybuff = []
lastx = 0

plt.ylabel('dBw')
plt.xlabel('Frequency')
plt.title("dBw vs. Frequency")

plt.ion()
fig, ax = plt.subplots()

while True:
    for line in sys.stdin:
        count += 1
        if line[0] == "#" or line[0] == '\n':
            continue
        point = list(map(float,line[:-1].split(' ')))
        x = point[0]
        # print(x)
        y = point[1]
        if x > lastx:
            xbuff.append(x)
            ybuff.append(y)
        else:
            ax.cla()
            ax.plot(xbuff, ybuff)
            plt.ylim([-135,-60])
            plt.pause(0.00000000001)
            plt.draw()
            xbuff = [x]
            ybuff = [y]
        lastx = x

print("wut?")
