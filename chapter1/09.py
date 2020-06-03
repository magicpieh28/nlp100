# Typoglycemia
import random


def typoglycemia(text: str):
    return ' '.join(
        [
            word[0] + ''.join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]
            if len(word) > 4 else word for word in text.split(' ')
        ]
    ).strip()


if __name__ == '__main__':
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(text))
