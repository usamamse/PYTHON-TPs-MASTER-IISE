class NegativeAgeError(Exception):
    pass

def set_age(age):
    try:
        if age > 0 :
            print(f'L\'age : {age}')
        else:
            raise NegativeAgeError("L'age doit etre positive")
    except NegativeAgeError as e:
        print(e)

set_age(15)
set_age(-15)