line = input("Enter your text: ")
counts = {}
for c in line:
    if counts.get(c):
        counts[c] += 1
    else:
        counts[c] = 1


def concat_by_colon(items):
    return ": ".join(map(str, items))


print(", ".join(map(concat_by_colon, counts.items())))


