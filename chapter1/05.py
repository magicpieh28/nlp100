# n-gram
def make_word_bi_gram(text: str):
    word_bi_gram = text.split(' ')
    return [word_bi_gram[i:i + 2] for i in range(len(word_bi_gram) - 1)]


def make_char_bi_gram(text: str):
    char_bi_gram = text.replace(' ', '')
    return [char_bi_gram[i:i+2]for i in range(len(char_bi_gram) - 1)]


if __name__ == '__main__':
    text = "I am an NLPer"
    print(make_word_bi_gram(text))
    print(make_char_bi_gram(text))
