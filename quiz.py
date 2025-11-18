
import json
import random

with open("questions.json", "r") as file:
    questions = json.load(file)

random.shuffle(questions)

score = 0

print("Welcome to the JSON Quiz Game!")
print("--------------------------------\n")

for q in questions:
    answer = input(q["question"] + " ").lower()

    if answer == q["answer"].lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer was: {q['answer']}\n")
print("--------------------------------")
print(f"You got {score} out of {len(questions)} correct!")
percentage = (score / len(questions)) * 100
print(f"Score: {percentage:.2f}%")