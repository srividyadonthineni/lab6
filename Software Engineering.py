def encode(password):
    shift = 0
    for i in password:
        i = int(i)
        i += (i+3)
    return password


def main():
    condition = True
    while condition:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        menu_option = int(input('Please enter an option: '))

        if menu_option == 1:
            encode_pass = input('Please enter your password to encode: ')
            if len(encode_pass) == 8:
                encoded = encode(encode_pass)
                print('Your password has been encoded and stored!')
            else:
                print('Your password is too long.')

        elif menu_option == 2:
            final = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {final}.')

        elif menu_option == 3:
            condition = False
            break


if __name__ == '__main__':
    main()
