# col1.txt, col2.txt
from pathlib import Path


def make_col_txt(txt_file: Path, row_num: int):
    with txt_file.open(mode="r") as txt:
        cols = [line.split('\t')[row_num - 1] for line in txt]
    with open(f"col{row_num}.txt", mode="w") as txt:
        for row in cols:
            txt.write(row + '\n')
        

if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    make_col_txt(txt_file, 1)
    make_col_txt(txt_file, 2)
