# 「パトカー」＋「タクシー」＝「パタトクカシーー」
def combine_str(text1: str, text2: str):
    return ''.join([t1 + t2 for t1, t2 in zip(text1, text2)])


if __name__ == '__main__':
    text1 = "パトカー"
    text2 = "タクシー"
    print(combine_str(text1, text2))
