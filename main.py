import colorama
from features.calculadora import *
from utils.typing_effects import typingEffect, typingEffectInput
from controller.user import User
from controller.validate import *
from controller.login import Login

colorama.init()

def main():
    email = typingEffectInput(colorama.Fore.WHITE + "Please, insert your email: ").strip()

    while validate_email(email) == False:
        typingEffect(colorama.Fore.RED + "Invalid email, try again.")
        email = typingEffectInput(colorama.Fore.WHITE + "Please, insert your email: ").strip()

    user = typingEffectInput(colorama.Fore.WHITE + "What's your name? ").strip()

    while validate_user(user) == False:
        typingEffect(colorama.Fore.RED + "Invalid username, try again.")
        user = typingEffectInput(colorama.Fore.WHITE + "What's your name? ").strip()

    password = typingEffectInput(colorama.Fore.WHITE + "Please, insert your password: ").strip()

    while validate_password(password) == False:
        typingEffect(colorama.Fore.RED + "Invalid password, try again.")
        password = typingEffectInput(colorama.Fore.WHITE + "Please, insert your password: ").strip()
    
    user = User(email, user, password)

    typingEffect(colorama.Fore.GREEN + "User created successfully!")

    typingEffect(colorama.Fore.WHITE + "To log into your account insert your email, username and password.")

    while Login().login(email=typingEffectInput(colorama.Fore.WHITE + "Email: "), user=typingEffectInput("Username: "), password=typingEffectInput("Password: ")) == False:
        typingEffect(colorama.Fore.RED + "Log in failed, try again.")

    typingEffect(colorama.Fore.GREEN + "Logged in successfully!")

    while typingEffectInput(colorama.Fore.WHITE + f"What do you want today, {user.get_user()}? Options: Calculator. ").capitalize() not in ["Calculator"]:
        typingEffect(colorama.Fore.RED + "That's not a valid option, try again.")

    while True:
        operation = typingEffectInput(colorama.Fore.WHITE + "Which type of calculator?\nSum\nSubtraction\nDivision\nMultiplication\nPower\n").capitalize()

        if operation == "Power":
            type_figure = typingEffectInput("Square, Cube...? ").capitalize()
            x = float(typingEffectInput("What's x? "))

            if type_figure == "Square":
                typingEffect(f"The power of {x}² = {power(x, 2)}")
            elif type_figure == "Cube":
                typingEffect(f"The power of {x}³ = {power(x, 3)}")
            else:
                typingEffect(colorama.Fore.RED + "Invalid power!")

        elif operation in ["Sum", "Subtraction", "Division", "Multiplication"]:
            try:
                x = float(typingEffectInput("What's x? "))
                y = float(typingEffectInput("What's y? "))

                if operation == "Sum":
                    typingEffect(f"The sum of {x} + {y} = {sum(x, y)}")
                elif operation == "Subtraction":
                    typingEffect(f"The subtraction of {x} - {y} = {subtract(x, y)}")
                elif operation == "Division":
                    typingEffect(f"The division of {x} / {y} = {divide(x, y):.2f}")
                elif operation == "Multiplication":
                    typingEffect(f"The multiplication of {x} * {y} = {multiply(x, y)}")
            
            except ValueError:
                typingEffect(colorama.Fore.RED + "Must be a number! Try again.")

        else:
            typingEffect(colorama.Fore.RED + "Looks like the calculator doesn't have that function yet! choose another")

if __name__ == "__main__":
    main()
