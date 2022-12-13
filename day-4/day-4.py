with open("sections.txt") as f:
    elf_sections = f.read().splitlines()

p1_overlap = 0
p2_overlap = 0

for pair in range(len(elf_sections)):
    elf_1, elf_2 = elf_sections[pair].split(",")
    start_1, end_1 = elf_1.split("-")
    start_2, end_2 = elf_2.split("-")
    start_1, end_1, start_2, end_2 = [int(x) for x in [start_1, end_1, start_2, end_2]]
    if start_1 <= start_2 and end_2 <= end_1 or start_2 <= start_1 and end_1 <= end_2:
        p1_overlap += 1
    if not(end_1 < start_2 or end_2 < start_1):
        p2_overlap += 1
print(p2_overlap)
