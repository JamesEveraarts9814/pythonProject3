# Functions go here


# Main routine goes here
def int_check(question):
    error = "Please enter an whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # If the amount is too low / too high give
            if 1 > response or response <=10:
                print("you have asked to play "
                      "with ${}".format(response))

                #output an error
            else:
                print(error)
        except ValueError:
            print(error)

how_much = int_check("How much would you like to play with? ")

