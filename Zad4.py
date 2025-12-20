import random
questions = [
    "Why is the sky blue?",
    "Why is the sun round?",
    "Where are all the dinosaurs?"
]
answer = ""

while answer != "to wszystko":
    question = random.choice(questions)

    answer = input(question + "\n> ")

    if answer != "to wszystko":
        print("dlaczego?\n")

print("\nkoniec")
