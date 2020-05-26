# the symbol of element
def make_sentence_as_list_of_elemnts(text: str):
    return {i: word[0] if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19] else word[:2]
            for i, word in enumerate(text.strip('.').split(' '))}


if __name__ == '__main__':
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. " \
           "Arthur King Can."
    print(make_sentence_as_list_of_elemnts(text))
