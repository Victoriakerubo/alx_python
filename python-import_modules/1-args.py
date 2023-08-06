import sys

def print_arguments(arguments):
    """Prints the arguments passed to the script."""
    number_of_arguments = len(arguments) - 1  # Exclude the script name
    print("{} argument{}:".format(number_of_arguments, "s" if number_of_arguments != 1 else ""), end="")
    if number_of_arguments == 0:
        print(".")
    else:
        for index, argument in enumerate(arguments[1:], start=1):  # Exclude the script name
            print("\n{}: {}".format(index, argument))

if __name__ == "__main__":
    arguments = sys.argv
    print_arguments(arguments)
