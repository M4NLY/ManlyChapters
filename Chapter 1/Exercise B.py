locations = ['Dubai','Paris', 'Switzerland', 'London', 'Amsterdam', 'New York']

#Print the list and its length

print(f"\nThis is the list of locations: {locations}. \nThe list has {len(locations)} locations.")

#Print the list in alphabetical order without modifying the list

sorted_loc = sorted(locations)
print(f"\nThis is the sorted list of locations: {sorted_loc}.")
print(f"This is the original list: {locations}")

#Reverse the list while being in alphabetical order

rev_loc = sorted(locations, reverse=True)
print(f"\nThis is the list of locations in reversed alphabetical order: {rev_loc}.")
print(f"This is the original list: {locations}")

#Change the order of the list with reverse()

locations.reverse()
print(f"\nThe list is permanently in reverse order: {locations}")

#Sort the list using sort()

locations.sort()
print(f"\nThis is the list of locations in alphabetical order: {locations}")

locations.sort(reverse=True)
print(f"\nThis is the list in reverse alphabetical order: {locations}")