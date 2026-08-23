# List of students
students_list = ["Shubham", "Aditya", "Keshaw"]
ages_list = [20, 21, 22]

# Add a student
students_list.append("Lily")
ages_list.append(23)
print("List after Add:", students_list, ages_list)

# Delete a student
students_list.remove("Aditya")
ages_list.remove(21)
print("List after Delete:", students_list, ages_list)

# Update a student
students_list[0] = "Martin"
ages_list[0] = 25
print("List after Update:", students_list, ages_list)


# Tuple of students
students_tuple = ("Shubham", "Aditya", "Keshaw")
ages_tuple = (20, 21, 22)

# Add a student to the tuple
y = list(students_tuple)
y.append("Lily")
students_tuple = tuple(y)

y = list(ages_tuple)
y.append(23)
ages_tuple = tuple(y)

print("Tuple after Add:", students_tuple, ages_tuple)


# Delete a student from the tuple
y = list(students_tuple)
y.remove("Aditya")
students_tuple = tuple(y)

y = list(ages_tuple)
y.remove(21)
ages_tuple = tuple(y)

print("Tuple after Delete:", students_tuple, ages_tuple)


# Update a student in the tuple
y = list(students_tuple)
y[0] = "Martin"
students_tuple = tuple(y)

y = list(ages_tuple)
y[0] = 25
ages_tuple = tuple(y)

print("Tuple after Update:", students_tuple, ages_tuple)


# Dictionary of students
students_dict = {
    "Shubham": 20,
    "Aditya": 21,
    "Keshaw": 22
}

# Add a student
students_dict["Lily"] = 23
print("Dictionary after Add:", students_dict)

# Delete a student
del students_dict["Aditya"]
print("Dictionary after Delete:", students_dict)

# Update a student
students_dict["Shubham"] = 25
print("Dictionary after Update:", students_dict)

