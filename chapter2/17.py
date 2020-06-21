# differences in first column
from pathlib import Path


def diff_in_first_col(txt_file: Path):
    with txt_file.open(mode="r") as f:
        first_col = [col.split("\t")[0] for col in f.readlines()]
    return set(first_col)


if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    print(diff_in_first_col(txt_file))
