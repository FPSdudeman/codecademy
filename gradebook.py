last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Lists of subjects and grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# 2D list of subjects and grades
gradebook = [
  ["physics", 98], 
  ["calculus", 97], 
  ["poetry", 85], 
  ["history", 88]
  ]
print(gradebook)

# Adding grades for 2 additonal courses
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Grade adjustment for visual arts
gradebook[-1][-1] += 5

# print(gradebook)

#Changing number grade to Pass/Fail for poetry
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Combining last semester and current gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
