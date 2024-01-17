import json

def write_to_json(stdnt_details):
    with open('StudentJson.json', 'w') as file:
        json.dump(stdnt_details, file)

def read_from_json():
    with open('StudentJson.json', 'r') as file:
        stdnt_details = json.load(file)
    return stdnt_details

# Get user input for student details
name = input("Enter student name: ")
stdnt_id = int(input("Enter student ID: "))
course = input("Enter student course: ")

# Create initial student details dictionary
stdnt_details = {
    "Name": name,
    "ID": stdnt_id,
    "Course": course
}

# Write the initial details to the JSON file
write_to_json(stdnt_details)

# Read the details from the JSON file
loaded_stdnt_details = read_from_json()

# Display the initial details
print("Details of the Student are")
for key, value in loaded_stdnt_details.items():
    print(f"\t{key}: {value}")

# Append additional CourseDetails
group = input("Enter course group: ")
course_year = int(input("Enter course year (Only Numbers): "))

loaded_stdnt_details["CourseDetails"] = {
    "Group": group,
    "Year": course_year
}

# Write the updated details to the JSON file
write_to_json(loaded_stdnt_details)

# Display the updated details
print("Details of the Student are:")
for key, value in loaded_stdnt_details.items():
    print(f"\t{key}: {value}")
