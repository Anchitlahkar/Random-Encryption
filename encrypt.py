from commands import init, select_code, encrypt_word

space, comma, symbols, characters, selected_code, used_no = init()


text = input("Word:\t")
print("\n\n")

def code():
    sp = list(text)


    space, comma, symbols, characters, selected_code, used_no = init()

    select_code(characters, symbols, selected_code, used_no)
    encrypted_word = encrypt_word(
        text_list=sp, characters=characters, selected_code=selected_code, used_no=used_no, comma=comma, space=space)

    print(encrypted_word)

    with open("key.txt", "w+", encoding='utf8') as f:
        f.write(encrypted_word)
		
    input("\n\nExit....")

code()
