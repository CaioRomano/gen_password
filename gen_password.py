import secrets
import string
import os


def generate_password(length: int = 15, special_characters: bool = False) -> str:
    """
    Função geradora de senha forte

    :param length: Número de caracteres presentes na senha gerada
    :param special_characters: Se gera ou não uma senha com caracteres especiais
    """

    alphabet = string.ascii_letters + string.digits + string.punctuation \
        if special_characters \
        else string.ascii_letters + string.digits

    password = ''.join(secrets.choice(alphabet) for i in range(length))

    return password


def save_password(password: str) -> None:
    """
    Salva a senha gerada num arquivo txt

    :param password: Senha gerada
    """

    filename = 'passwords.txt'

    if not os.path.exists(filename):
        with open(filename, 'w') as arq:
            pass

    with open(filename, 'r+') as arq:
        passwords_created = [row.split('\n')[0] for row in arq.readlines()]
        if len(passwords_created) == 0:
            print(f'Primeira senha: {password}\n')
            arq.write(f'{password}\n')
        else:
            if password in passwords_created:
                print('Senha já existe!')
            else:
                arq.write(f'{password}\n')
                print(password)


if __name__ == '__main__':
    password = generate_password(45, False)
    save_password(password)
