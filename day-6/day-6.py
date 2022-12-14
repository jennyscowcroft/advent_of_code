with open("datastream.txt") as f:
    datastream = f.read()

count = 4
for i in range(4, len(datastream)):
    four_bits = set(datastream[(i-4):i])
    if len(four_bits) == 4:
        print(i)
        break

for i in range(18, len(datastream)):
    four_bits = set(datastream[(i-14):i])
    if len(four_bits) == 14:
        print(i)
        break

