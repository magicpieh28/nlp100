# print nth column
from pathlib import Path


def select_column(txt_file: Path, n: int):
    with txt_file.open(mode="r") as txt:
        selected = txt.readlines()[n - 1]
    return selected


if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    print(select_column(txt_file, 24))
