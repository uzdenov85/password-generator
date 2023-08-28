import random

SMALL_LETTERS = 'abcdefghkmnpqrstuvwxyz'
CAPITAL_LETTERS = SMALL_LETTERS.upper()
DIGITS = '0123456789'
SYMBOLS = '?#@$%&-*'
ALPHANUMERIC_SYMBOLS = SMALL_LETTERS + CAPITAL_LETTERS + DIGITS + SYMBOLS


def main():
    generator_mode = int(input('Select mode: \n 1. Generate and write to file \n 2. Just generate \n : '))
    if generator_mode == 1:
        password_filename = str(input('Type file name (default passwords.txt): '))
        if password_filename != 'passwords.txt' and password_filename != '':
            pass
        else:
            password_filename = 'passwords.txt'
        
        password_file = open(password_filename, 'a')
        resource_name = str(input('Please type resource name: '))
        resource_url = str(input('Please type url: '))
        resource_credentials = str(input('Please type resource credentials: '))
        password_length = int(input('Type password length: '))
        while  password_length < 8 or password_length > 32:
            print('Password must be at least 8 and no more than 32 character.')
            password_length = int(input('Type password length: '))
        
        generated_password = generate_password(password_length)
        password_file.write(resource_name + ', ' + resource_url + ', ' +  resource_credentials + ', ' + generated_password + '\n')
        add_one_more = str(input('Add one more? Yes/Y/y|No/N/n (default: No): '))
        if add_one_more == 'Yes' or add_one_more == 'yes' or add_one_more == 'Y' or add_one_more == 'y':
            main()
        else:
            pass
    else:
        password_length = int(input('Please type password length: '))
        generated_password = generate_password(password_length)
        print(generated_password)
                           
def generate_password(length):
    password = ''.join(random.sample(ALPHANUMERIC_SYMBOLS,length))
    return password

def run():
    main()

run()