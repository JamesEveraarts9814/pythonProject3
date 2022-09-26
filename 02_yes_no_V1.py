
#Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response  == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
             response = "no"
             return response
        else:
            print("Please enter yes or no")



# Main routine goes here

show_instructions = ""
while show_instructions!= "xxx":
    # Ask user if they have played before
    # If they say no, output 'display instructions'
    # If they say yes, output 'program continues'
    show_instructions = yes_no("Have you played this game before? ")
    print("You chose {}".format(show_instructions))
