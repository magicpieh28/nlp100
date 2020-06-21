# print nth record
from pathlib import Path


def select_record(txt_file: Path, n: int):
    with txt_file.open(mode="r") as txt:
        selected = txt.readlines()[n - 1]
    return selected


if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    print(select_record(txt_file, 24))
