
# Generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
-Please make sure your Integer doesn't have any decimals 
 and is between (or equal to) 1 and 200.
-put the Integer into the program.
-type "xxx" if you wish to exit the program.
    ''')


def num_check(question):

    error = "Please make sure your number doesn't have any decimals" \
            " and is between (or equal to) 1 and 200 :)\n"
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
    factors_list = []
    to_factor = num_check("To factor: ")

    # square root the number to work out when to stop looping.
    stop = round()
    stop = int(stop)
    for item in range(1, 200):

        # check to see if the item is a factor
        if to_factor

        # calculate partner
        partner =

        # add partner to the list (but prevent duplicates)
        if partner:
            factor(var_to_factor).append(factors_list)

    # return sorted list
    factors_list.sort()
    return factors_list


# Main routine goes here
statement_generator("The Ultimate Factor Finder", "-")
want_instructions = input("Press <enter> to read the instructions " "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues\n")

comment = ""
while True:
    to_factor = num_check("\n Enter an integer (Or xxx to quit): ")
    print("You choose to factor: ", to_factor)

    if to_factor == "xxx":
        break

    elif to_factor != 1:
        all_factors = factor(to_factor)

    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor, itself :D"

    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number :D"

    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square!"

    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)



print("Thank you for using the factors calculator :)")
