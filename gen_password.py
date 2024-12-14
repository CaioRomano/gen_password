import secrets
import string


def generate_password(length: int = 10) -> None:
    """
    Função geradora de senha forte

    :param length: Número de caracteres presentes na senha gerada
    """

    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    print(password)


if __name__ == '__main__':
    generate_password(25)
