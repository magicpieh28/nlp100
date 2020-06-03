# count columns
from pathlib import Path


def count_columns(txt_file: Path):
    with txt_file.open(mode="r") as txt:
        count = txt.readlines().__len__()
    return count
        

if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    print(count_columns(txt_file))
