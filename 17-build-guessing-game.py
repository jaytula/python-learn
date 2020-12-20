secret_word = "giraffe"
guess = ""
guess_limit = 10
guess_count = 0

while guess != secret_word and guess_count < guess_limit:
    guess = input("Enter guess " + str(guess_count + 1) + " : ")
    guess_count += 1
    if guess == secret_word:
        print("You got it!")
        break
    if guess_count == guess_limit:
        print("You ran out of guesses")

