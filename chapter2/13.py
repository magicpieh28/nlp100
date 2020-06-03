# merge cols
from pathlib import Path


def merge_cols(txt1: Path, txt2: Path):
    with txt1.open(mode="r") as txt1, txt2.open(mode="r") as txt2:
        merged_cols = ['\t'.join(cols) for cols in zip(txt1, txt2)]
    with open("cols.txt", mode="w") as txt:
        for cols in merged_cols:
            txt.write(cols + '\n')
            
            
if __name__ == '__main__':
    txt_file1 = Path(__file__).resolve().parent / 'col1.txt'
    txt_file2 = Path(__file__).resolve().parent / 'col2.txt'
    merge_cols(txt_file1, txt_file2)