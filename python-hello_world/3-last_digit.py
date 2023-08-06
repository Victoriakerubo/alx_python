def last_digit(number):
  """
  Prints the last digit of a number.

  Args:
    number: The number whose last digit to print.

  Returns:
    The last digit of the number.
  """

  last_digit = abs(number) % 10

  if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
  elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
  else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

if __name__ == "__main__":
  number = random.randint(-10000, 10000)
  last_digit(number)
