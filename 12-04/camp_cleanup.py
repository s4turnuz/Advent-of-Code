def _inside(a, b):
    return a[0] >= b[0] and a[1] <= b[1]

# Get data
f = open('12-04/elf_pair.txt').read()

elf_pair = 0

for line in f.split("\n"):
    first, second = line.split(",")

    f1, f2 = first.split("-")
    f3, f4 = second.split("-")

    # Wrong....
    # list1 = list(range(f1, f2+1))
    # list2 = list(range(f3, f4+1))
    # inters = set(list1) & set(list2)

    a = int(f1), int(f2)
    b = int(f3), int(f4)

    elf_pair += 1 if _inside(a, b) or _inside(b, a) else 0

print(elf_pair)
elf_pair = 0    #clear


## PART TWO


# only change
def laps(a, b):
    return a[1] >= b[0] and a[0] <= b[1]


for line in f.split("\n"):
    first, second = line.split(",")

    f1, f2 = first.split("-")
    f3, f4 = second.split("-")

    a = int(f1), int(f2)
    b = int(f3), int(f4)

    elf_pair += 1 if laps(a, b) else 0

print(elf_pair)
