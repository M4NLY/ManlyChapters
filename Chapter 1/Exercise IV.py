staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

print(f"\n{staff}\n")
staff_count = {}

for member in staff:
    if member in staff_count:
        staff_count[member] += 1
    else:
        staff_count[member] = 1

for member, count in staff_count.items():
    print(f"{member}: {count} times")
