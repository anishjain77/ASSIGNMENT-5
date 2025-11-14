# Step 1: Create a dictionary of students and their marks
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 76
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve marks or show message if not found
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found!")
