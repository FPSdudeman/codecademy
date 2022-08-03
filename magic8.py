import random

# Codecademy won't let me use "input()" so name and question vars here
name = "Tyler"
question = "Can I has water?"

# Using the "random" module to generate a random number from 1-9 
random_number = random.randint(1,9)
# test case - print(random_number)

# possible answers from a dict var "answer"
answer = {
  1: "Yes - definitely.",
  2: "It is decidedly so.",
  3: "Without a doubt",
  4: "Reply hazy, try again.",
  5: "Ask again later.",
  6: "Better not tell you now.",
  7: "My sources say no.",
  8: "Outlook not so good.",
  9: "Very doubtful."
}

# Verify there is a question
if question == "":
  print("You need to ask a question or the very fabric of reality is at risk by using me!")
  exit()

# If there is no name just pring question. If there is both print both.
if name == "":
  print("Question: " + question)
elif len(name) > 1:
  print(name + " asks: " + question)

# Print random response or else print error
if random_number <= 9:
  print("Magic 8-Ball's answer: " + answer[random_number])
else:
  print("Error")
