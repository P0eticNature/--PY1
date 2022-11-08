import random
import string

def get_random_password() -> str:
    n = 8
    generator = string.ascii_lowercase + string.ascii_uppercase + string.digits
    randomize = random.sample(generator, n)
    password = "".join([str(keys) for keys in randomize])
    return password

# TODO написать функцию генерации случайных паролей


print(get_random_password())
