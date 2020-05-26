# pi
def build_list_of_words_len(text: str):
    return [len(word) for word in text.strip('.,').split(' ')]


if __name__ == '__main__':
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(build_list_of_words_len(text))
