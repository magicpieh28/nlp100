# tab to space
from pathlib import Path


def tab2space(txt_file: Path):
    with txt_file.open(mode="r") as txt:
        with_spaces = [line.replace('\t', ' ') for line in txt]
    return with_spaces


if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    print(tab2space(txt_file))
