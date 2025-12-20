import random

def random_Capital_letter():
    """Returns a random capital letter from A to Z."""
    return chr(random.randint(ord('A'), ord('Z')))

def random_lowercase_letter():
    """Returns a random lowercase letter from a to z."""
    return chr(random.randint(ord('a'), ord('z')))

def random_digit():
    """Returns a random digit from 0 to 9."""
    return chr(random.randint(ord('0'), ord('9')))

def random_special_character():
    """Returns a random special character from the specified set."""
    special_characters = "!@#$%^&*()-_=+[]/{}|;:',.<>?/"
    return random.choice(special_characters)

def get_lowercase_uppercase_pattern():
    """Generates a pattern with one random lowercase and one random uppercase letter."""
    lowercase = random_lowercase_letter()
    uppercase = random_Capital_letter()
    return lowercase + uppercase

cars3 = random_digit()
cars2 = random_special_character()
cars_a = get_lowercase_uppercase_pattern()
cars_b = get_lowercase_uppercase_pattern()
cars_c = get_lowercase_uppercase_pattern()
cars_d = get_lowercase_uppercase_pattern()
cars_e = get_lowercase_uppercase_pattern()
cars_f = get_lowercase_uppercase_pattern()
cars_g = get_lowercase_uppercase_pattern()
cars_h = get_lowercase_uppercase_pattern()
cars_i = get_lowercase_uppercase_pattern()

print(cars_a+cars_b+cars_c+cars_d+cars_e+cars_f+cars_g+cars_h+cars_i+cars3+cars2)