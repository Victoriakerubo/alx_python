import sys

# Get the number of arguments (excluding the script name)
num_arguments = len(sys.argv) - 1

# Print the number of arguments
print("{} argument{}".format(num_arguments, "s" if num_arguments != 1 else ""), end="")

# Print ":", "." or newline based on the number of arguments
if num_arguments == 0:
    print(".")
else:
    print(":")
    for i in range(1, num_arguments + 1):
        print("{}: {}".format(i, sys.argv[i]))
