# Generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


statement_generator("The Ultimate Factor Finder", "-")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
-Please make sure your Integer doesn't have any decimals 
 and is between (or equal to) 1 and 200.
-put the Integer into the program.
-type "xxx" if you wish to exit the program.
    ''')

# Main routine goes here


want_instructions = input("Press <enter> to read the instructions " "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues\n")


def num_check(question):

    error = "Please make sure your number doesn't have any decimals" \
            "and is between (or equal to) 1 and 200 :)\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here
while True:
    to_factor = num_check("To factor: ")
    print("You choose to factor", to_factor)

    if to_factor == "xxx":
        break
