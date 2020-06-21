# split file by n
from pathlib import Path


def split_txt_file(txt_file: Path):
    with txt_file.open(mode="r") as f:
        num = int(input("input n: "))
        records = f.readlines()
        n_in_one_file = (len(records) / num).__round__()
        
        split_txts = [
            [line for line in records[n_in_one_file * n: n_in_one_file * n + n_in_one_file]] for n in range(num)
        ]
        
    for i in range(num):
        with open(Path(__file__).resolve().parent / f'split_result_{i+1}', mode='w', newline='') as f:
            f.writelines(split_txts[i])
            
            
if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    split_txt_file(txt_file)
