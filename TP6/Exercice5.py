def process_input(user_input):
    try:
        if isinstance(user_input, (int, float)) and user_input == int(user_input):
            print(f'{int(user_input) / 10}')
        elif isinstance(user_input, str) and user_input.isnumeric():
            print(f'{int(user_input) / 10}')
        else:
            raise ValueError("Entrée invalide : doit être un nombre entier ou une chaîne numérique.")
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Erreur : division par 0.")

process_input(100)
process_input(20.0)
process_input("10")
process_input("Hello")