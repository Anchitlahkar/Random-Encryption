from commands import init

space, comma, symbols, characters, selected_code, used_no = init()


def decrypt():
    en_word = encrypted_word.split("𓈠")[1]
    word = ""
    sp_en_word = list(en_word)

    for i in sp_en_word:
        idx = selected_code.index(i)
        word += str(characters[idx])

    return word

try:
    file = open("key.txt", "r",encoding='utf8')
    encrypt_word = file.readlines()

except FileNotFoundError:
    print("key.txt wan not found.")

encrypted_word = encrypt_word[0]




def select_code():
    word = encrypted_word.split("𓈠")[0]
    word_1 = word.split("𓈡")

    if "" in word_1:
        word_1.remove("")

    elif " " in word_1:
        word_1.remove(" ")

    for i in range(len(word_1)):
        index = word_1[i]
        idx = int(index)
        
        selected_code.append(symbols[idx])



select_code()

ans = decrypt()
print(ans)
input("\n\nExit....")




