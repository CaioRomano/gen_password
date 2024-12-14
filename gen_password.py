import secrets
import string


def generate_password(length: int = 15, special_characters: bool = False) -> None:
    """
    Função geradora de senha forte

    :param length: Número de caracteres presentes na senha gerada
    :param special_characters: Se gera ou não uma senha com caracteres especiais
    """

    alphabet = string.ascii_letters + string.digits + string.punctuation \
        if special_characters \
        else string.ascii_letters + string.digits

    password = ''.join(secrets.choice(alphabet) for i in range(length))
    print(password)


if __name__ == '__main__':
    generate_password(25, True)
