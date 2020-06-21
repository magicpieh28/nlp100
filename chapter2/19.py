# sort by frequency of first column
from pathlib import Path


def sort_records_by_region_freq(txt_file: Path):
    with txt_file.open(mode="r") as f:
        table = [record.strip('\n').split('\t') for record in f.readlines()]
        
    region_freq = {record[0]: 0 for record in table}
    for record in table:
        if record[0] in region_freq.keys():
            region_freq[record[0]] += 1
    region_freq = [k for k, _ in sorted(region_freq.items(), key=lambda record: record[1], reverse=True)]
    
    return sorted(table, key=lambda record: region_freq.index(record[0]))


if __name__ == '__main__':
    txt_file = Path(__file__).resolve().parent / 'hightemp.txt'
    print(sort_records_by_region_freq(txt_file))
