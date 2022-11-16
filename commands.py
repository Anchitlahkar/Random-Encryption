import random


def init():
    space = "𓈠"
    comma = "𓈡"

    symbols = [
        "𓀀", "𓀁", "𓀂", "𓀃", "𓀄", "𓀅", "𓀆", "𓀇", "𓀈", "𓀉", "𓀊", "𓀋", "𓀌", "𓀍", "𓀎", "𓀏",
        "𓀐", "𓀑", "𓀒", "𓀓", "𓀔", "𓀕", "𓀖", "𓀗", "𓀘", "𓀙", "𓀚", "𓀛", "𓀜", "𓀝", "𓀞", "𓀟",
        "𓀠", "𓀡", "𓀢", "𓀣", "𓀤", "𓀥", "𓀦", "𓀧", "𓀨", "𓀩", "𓀪", "𓀫", "𓀬", "𓀭", "𓀮", "𓀯",
        "𓀰", "𓀱", "𓀲", "𓀳", "𓀴", "𓀵", "𓀶", "𓀷", "𓀸", "𓀹", "𓀺", "𓀻", "𓀼", "𓀽", "𓀾", "𓀿",
        "𓁀", "𓁁", "𓁂", "𓁃", "𓁄", "𓁅", "𓁆", "𓁇", "𓁈", "𓁉", "𓁊", "𓁋", "𓁌", "𓁍", "𓁎", "𓁏",
        "𓁐", "𓁑", "𓁒", "𓁓", "𓁔", "𓁕", "𓁖", "𓁗", "𓁘", "𓁙", "𓁚", "𓁛", "𓁜", "𓁝", "𓁞", "𓁟",
        "𓁠", "𓁡", "𓁢", "𓁣", "𓁤", "𓁥", "𓁦", "𓁧", "𓁨", "𓁩", "𓁪", "𓁫", "𓁬", "𓁭", "𓁮", "𓁯",
        "𓁰", "𓁱", "𓁲", "𓁳", "𓁴", "𓁵", "𓁶", "𓁷", "𓁸", "𓁹", "𓁺", "𓁻", "𓁼", "𓁽", "𓁾", "𓁿",
        "𓂀", "𓂁", "𓂂", "𓂃", "𓂄", "𓂅", "𓂆", "𓂇", "𓂈", "𓂉", "𓂊", "𓂋", "𓂌", "𓂍", "𓂎", "𓂏",
        "𓂐", "𓂑", "𓂒", "𓂓", "𓂔", "𓂕", "𓂖", "𓂗", "𓂘", "𓂙", "𓂚", "𓂛", "𓂜", "𓂝", "𓂞", "𓂟"
    ]

    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '}', '{', '^', '[', ']', ' ', '+', '-', '_',
                  '&', ';', '"', '?', '`', "'", '\\',",","—"]

    selected_code = []
    used_no = []

    return space, comma, symbols, characters, selected_code, used_no


def select_code(characters, symbols, selected_code, used_no):
    for i in range(len(characters)):
        idx = random.randint(0, len(characters))

        if idx in used_no:
            idx = random.randint(0, len(characters))
            selected_code.append(symbols[idx])
            used_no.append(idx)

        else:
            selected_code.append(symbols[idx])
            used_no.append(idx)


def encrypt_word(text_list, characters, selected_code, used_no, comma, space):
    word = ""

    for i in used_no:
        word += f"{i}{comma}"

    word += space

    for i in text_list:
        try:
            idx = characters.index(i)
            word += str(selected_code[idx])
        except:
            idx = characters.index(" ")
            word += str(selected_code[idx])

    return word


def form_encrypt_txt(word):
    pass



