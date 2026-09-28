words = {
    "Hallo": "hello",
    "Danke": "thank you",
    "Ja": "yes",
    "Nein": "no",
    "Tschüss": "bye",
}

score = 0
print("Welcome to the German vocabulary quiz!")

for german, english in words.items():
    answer = input(f"What does '{german}' mean? ")
    if answer.strip().lower() == english:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The answer is: {english}")

print(f"Your score: {score} out of {len(words)}")