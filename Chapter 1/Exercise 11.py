year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

#Access the value at -3

print(f"\nThe year at the index value -3 is {year[-3]}.")

#Reverse the tuple and print the original tuple and reversed tuple

print(f"\nThis is the original order of the tuple: {year}.")

rev_tuple = year[::-1]
print(f"\nThis is the reversed order of the tuple: {rev_tuple}.")

#Count the number of times 2009 appears

print(f"\n2009 appears in the tuple {year.count(2009)} times.")

#Get the index value of 2018

print(f"\n2018 has the index value of {year.index(2018)}.")

#Find the length of the list

print(f"\nThe tuple has {len(year)} years.")