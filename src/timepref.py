from time import perf_counter

start = perf_counter()
for i in range(1000000):
    pass
end = perf_counter()
print(end - start)