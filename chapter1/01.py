# パタトクかシーー
def extract_taxi(text: str):
    return text[1::2]


if __name__ == '__main__':
    text = "パタトクかシーー"
    print(extract_taxi(text))
