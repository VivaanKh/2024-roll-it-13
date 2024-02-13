# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not choose a valid response.")


# Main routine
while True:
    want_instructions = yes_no("Do you want to read the instructions? (answer yes or no) ")
    print(f"you chose {want_instructions}")
# go on video 4