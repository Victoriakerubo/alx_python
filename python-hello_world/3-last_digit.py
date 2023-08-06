import random

def last_digit_properties(number):
    last_digit = abs(number) % 10

    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    else:
        print(f"Last digit of {number} is -{last_digit} and is less than 6 and not 0")

if __name__ == "__main__":
    last_digit_properties(4205)
    last_digit_properties(-626)
    last_digit_properties(1144)
    last_digit_properties(-9200)
    last_digit_properties(5247)
    last_digit_properties(-9318)
    last_digit_properties(3369)
    last_digit_properties(-5224)
    last_digit_properties(-4485)
    last_digit_properties(3850)
    last_digit_properties(5169)
