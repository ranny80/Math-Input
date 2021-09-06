number = "5"
multiply = int(number) * 5
tries = 0

def outoftries():
    print("Sorry, you've got ran out of tries.")

print(multiply)

print("Wait, how did you multiply?")
answer = input("Enter your answer: ")

if answer == "5":
    print("Ok, you've got it right!")
else:
    print("That's not the answer. Please try again.")
    tries = tries + 1

    answer = input("Enter your answer: ")

    if answer == "5":
        print("Ok, you've got it right!")
    else:
        print("That's not the answer. Please try again.")
        tries = tries + 1

        answer = input("Enter your answer: ")

        if answer == "5":
            print("Ok, you've got it right!")
        else:
            tries = tries + 1
            outoftries()
