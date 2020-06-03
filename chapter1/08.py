# encryption
def cipher(text: str):
    return ''.join(str(219 - ord(char)) if char.islower() else char for char in text)


if __name__ == '__main__':
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine"
    print(cipher(text))
