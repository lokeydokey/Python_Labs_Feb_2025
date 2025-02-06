
def frange(start, stop,step=0.25):
    i = float(start)
    if step == 0:
        return []
    while i < stop:
        yield i
        i += step

print(list(frange(1.1, 3)))
print(list(frange(1, 3, 0.33)))
print(list(frange(1, 3, 1))) # Should print [1.0, 2.0]
print(list(frange(3, 1)))
print(list(frange(1, 3, 0)))
print(list(frange(-1, -0.5, 0.1)))

for num in frange(3.142, 12):
    print(f"{num:05.2f}")

print (frange (1,2))
print (frange (1,2))