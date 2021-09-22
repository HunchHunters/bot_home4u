
g = ([1,2,3])

try:
    while True:
        item = next(g)
        print(item)
except StopIteration:
    print("Items ended")
