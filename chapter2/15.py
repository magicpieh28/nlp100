# print last nth record
from pathlib import Path


def select_last_record(txt_file: Path):
    with txt_file.open(mode="r") as f:
        record = f.readlines()[-int(input("input which record you want: "))]
    return record


if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    print(select_last_record(txt_file))
