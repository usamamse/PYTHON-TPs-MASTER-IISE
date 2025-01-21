def convert_to_int(value):
    if isinstance(value, (int,float)) and value == int(value):
        return int(value)
    elif isinstance(value, str) and value.isnumeric():
        return int(value)
    else:
        raise ValueError("Erreur de conversion")

print(convert_to_int("22"))
print(convert_to_int(22))
print(convert_to_int(22.0))
print(convert_to_int("Hello"))

