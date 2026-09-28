import random

words = {
    "Hallo": "hello",
    "Danke": "thank you",
    "Ja": "yes",
    "Nein": "no",
    "Tschüss": "bye",
    "Bitte": "please",
    "Entschuldigung": "sorry",
    "Guten Tag": "good day",
}

items = list(words.items())
random.shuffle(items)

score = 0
print("Welcome to the German vocabulary quiz!")

for german, english in items:
    answer = input(f"What does '{german}' mean? ")
    if answer.strip().lower() == english:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The answer is: {english}")

print(f"Your score: {score} out of {len(items)}")