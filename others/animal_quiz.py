def check_guess(guess,answer):
    global score
    still_guess = True
    attempt = 0
    while still_guess and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer!")
            score = score + 1
            still_guess = False
        else:
            if attempt < 2:
                guess = input("Wrong answer. Try again. ")
            attempt = attempt + 1

        if attempt == 3:
            print(f"The coorect answer is {answer}.")

def test(quesion, answer):
    print(quesion,end='')  # doesn't end
    guess = input()
    check_guess(guess,answer)

print("Let's guess the animal.\n")

score = 0
test("Which bear lives in North Pole? ","polar bear")
test("Which is the fastest land animal? ","cheetah")
test("Which is the largest animal? ","blue whale")

print("\n")  # add new line
print(f"Game over. Your score is {str(score)}.")