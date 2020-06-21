# sort records by third column
from pathlib import Path


def sort_records_by3(txt_file: Path):
    with txt_file.open(mode="r") as f:
        table = [record.strip('\n').split('\t') for record in f.readlines()]
    return sorted(table, key=lambda record: record[2], reverse=True)
    

if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    print(sort_records_by3(txt_file))
