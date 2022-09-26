

# Function goes here
def yes_no (question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game goes here")
    print()
    return ""

# Main route goes here
show_instructions = yes_no("Have you played the game before?")


if show_instructions == "No":
    instructions()

print("Program continues")
