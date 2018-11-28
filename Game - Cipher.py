def cipher():
    action = input('Do you wish to encrypt or decrypt a message? ').lower()
    message = input('Enter your message: ')
    key = int(input('Enter the key number (1-52) '))

    alpha_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    alpha_list = list(alpha_string)
    shifted_list = []
    for i in range(0,52):
        shifted_list.append(alpha_list[i+key])
    zipped_dict = dict(zip(alpha_list,shifted_list))

    encrypted_message = []
    if action == 'encrypt' or action == 'e':
        for letter in message:
            if letter not in alpha_list:
                encrypted_message.append(letter)
            else:
                encrypted_message.append(zipped_dict[letter])
        encrypted_message= ''.join(encrypted_message)
        print(encrypted_message)

    decrypted_message = []
    if action == 'decrypt' or action == 'd':
        for letter in message:
            if letter not in alpha_list:
                decrypted_message.append(letter)
            else:
                decrypted_message.append([key for key, value in zipped_dict.items() if value == letter][0])
        decrypted_message= ''.join(decrypted_message)
        print(decrypted_message)

cipher()