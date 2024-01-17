marks = [
    ("CodeLab I", 67),
    ("Web Development", 75),
    ("CodeLab II", 74),
    ("Smartphone Apps", 68),
    ("Games Development", 70),
    ("Responsive Web", 65)
]

low_high = sorted(marks, key=lambda x: x[1])
high_low = sorted(marks, key=lambda x: x[1], reverse=True)

print(f"\nThe grades are sorted from lowest to highest: {low_high}")
print(f"\n The grades are sorted from highest to lowest: {high_low}")

