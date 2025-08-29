def get_valid_number(prompt, min_value=None, max_value=None):
    while True:
        try:
            user_input = int(input(prompt))
            if not min_value and not max_value:
                return user_input
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


import random  
def generate_random_list(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]

