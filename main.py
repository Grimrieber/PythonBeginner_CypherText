
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def cypher_text():
    do = input('''Type 'encode' to encrypt, type 'decode' to decrypt:\n''').lower()

    if do == "encode":
        msg = input("Type your message to encode:\n")
        shift_number = int(input("Type the shift number:\n"))
        encode_msg = ""
            
        for letter in msg:
            position = alphabet_list.index(letter)
            new_position = position + shift_number


            while new_position > len(alphabet_list):
                new_position -= len(alphabet_list)
            
            encode_msg += alphabet_list[new_position]
            
        print(encode_msg)
    elif do == "decode":
        msg = input("Type message to decode:\n")
        shift_number = int(input("Type the shift number:\n"))
        decode_msg = ""

        for letter in msg:
            position = alphabet_list.index(letter)
            new_position = position - shift_number

            while new_position < 0:
                new_position += len(alphabet_list)
            
            decode_msg += alphabet_list[new_position]
        print(decode_msg)

    else:
        print("You have not entered a valid entry. Please try again.")
        cypher_text()


cypher_text()