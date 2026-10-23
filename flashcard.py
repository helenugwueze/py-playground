print("================================")
print("       FLASHCARD QUIZ TOOL")
print("================================")

print("Welcome to the Flashcard Quiz!")

name = input("What is your name? ")
print("Hello,", name + "!", "Let's begin.")

questions = [
    ("What is the French word for Hello?", "bonjour"),
    ("What is 5 + 3?", "8"),
    ("What language are we learning?", "python"),
    ("What is the capital of Nigeria?", "abuja"),
    ("What is 10 - 4?", "6")
]

score = 0

for question, answer in questions:
    print("\nQuestion:", question)
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == answer.lower():
        print("Correct! Well done!")
        score = score + 1
    else:
        print("Sorry, that is incorrect.")
        print("The correct answer is:", answer)

    print("Your current score:", score)

print("\n================================")
print("           QUIZ RESULTS")
print("================================")
print("Player:", name)
print("Final score:", score, "out of", len(questions))

if score == len(questions):
    print("Excellent! You got every question right!")
elif score >= 3:
    print("Good job! Keep practising.")
else:
    print("Keep learning! You can do better next time.")

print("Thank you for playing!")

