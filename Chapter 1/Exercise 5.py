count = 0

while True:
    ans = input("\nWould you like to continue? (Y/N): ").strip().upper()
    
    if ans != "Y":
        break
    
    count += 1
    
print(f"\nThis occured {count} times.")