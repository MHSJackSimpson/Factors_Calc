
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


def factor(var_to_factor):
    pass


while True:
    to_factor = num_check("To factor: ")
    print("You choose to factor", to_factor)

    if to_factor == "xxx":
        break
    elif to_factor != 1:
        all_factors = factor(to_factor)

    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor, itself :D"

    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number!"

    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square!"

    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    print()
    statement_generator(heading, "-")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator :)")
