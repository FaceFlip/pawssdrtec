import sys
import time
import numpy

current_milli_time = lambda: int(round(time.time() * 1000))

count = 10
sweep_count = 0
delays_array = []

target_sweep_count = 100
time1 = current_milli_time()
while True:
    for line in sys.stdin:
        count += 1
        if line[0] == "#":
            if count > 10:
                count = 0
                time2 = current_milli_time()
                delay = time2-time1
                delays_array.append(delay)
                print(f"Sweep {sweep_count:3}:", time2-time1, "ms" )
                if sweep_count >= target_sweep_count:
                    break
                sweep_count += 1
                time1 = current_milli_time()
    if sweep_count >= target_sweep_count:
        break

nd = numpy.array(delays_array[1:])
print("=============================================")
print("Number of Trials:", target_sweep_count)
print("Average delay:", int(numpy.mean(nd)), "ms")
print("Standard deviation:", int(numpy.std(nd)), "ms")
print("Total time elapsed:", int(numpy.sum(nd)), "ms")
