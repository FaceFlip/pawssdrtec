import matplotlib.pyplot as plt
import numpy as np
import sys
import time

while True:
    time.sleep(1)
    buff = sys.stdin.read()
    if len(buff) != 0:
        print("HI")
        data = buff.replace("\n", "").split(",")
        startFreq = float(data[2])
        endFreq = float(data[3])

        yCords = list(map(float,data[6:]))

        numSamples = len(data[6:])
        sampleSize = (endFreq-startFreq)/numSamples
        xCords = []
        for i in range(numSamples):
            xCords.append(startFreq + i*sampleSize)

        plt.plot(xCords, yCords, label='Stuff')
            # plt.plot(x, x**2, label='quadratic')
            # plt.plot(x, x**3, label='cubic')

        plt.xlabel('Frequency')
        plt.ylabel('dBw')

        plt.title("dBw vs. Frequency")

        plt.legend()

        plt.show()
