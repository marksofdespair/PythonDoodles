last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# forgot task 7, modifying the grade for 'visual arts' by adding 5 points
gradebook[-1][1] += 5

print (gradebook)
# Locate the sublist for "poetry"
poetry_entry = gradebook[2]

# Use .remove() to remove the grade value (85)
poetry_entry.remove(85)
poetry_entry.append("Pass")
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)
