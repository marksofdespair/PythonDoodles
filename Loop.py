# While Loop Walkthrough
# count = 0
# print("Starting While Loop")
# while count <= 3:
#   # Loop Body
#   # Print if the condition is still true
#   print("Loop Iteration - count <= 3 is still true")
#   # Print the current value of count 
#   print("Count is currently " + str(count))
#   # Increment count
#   count += 1
#   print(" ----- ")
# print("While Loop ended")

# My code below: 
countdown = 10
while countdown >= 0: 
  print(countdown)
  countdown -= 1 
print("We have liftoff!")

# ---------------------------------------------------------------------------------

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# Variable to represent the length of the list
length = len(python_topics)

# Create a variable called index and initialize the value to be 0.
index = 0

while index < length:
  print("I am learning about " + python_topics[index])
  index += 1

# ---------------------------------------------------------------------------------

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

# Uncommenting line 44 will cause an infinite loop and explode ur IDE

for student in students_period_A:
  # students_period_A.append(student)
  print(student)

# ---------------------------------------------------------------------------------

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
