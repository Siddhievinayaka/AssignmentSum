# Create a Personalized Greeting
def personalized_greeting(name, s_name):
    return f"\nHello, {name} {s_name}! Welcome to the Python course."


# Example usage
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")

greeting = personalized_greeting(first_name, surname)
print(greeting)
