import sys

def print_arguments(arguments):
  """Prints the arguments passed to the script."""
  print("{} arguments:".format(len(arguments)))
  for index, argument in enumerate(arguments):
    print("{}: {}".format(index + 1, argument))

if __name__ == "__main__":
  arguments = sys.argv
  print_arguments(arguments)
