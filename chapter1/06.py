# set
from typing import Set


def make_bi_gram(text: str):
    return [text[i:i+2] for i in range(len(text) - 1)]


def set2list(set_arg: set):
    return [arg for arg in set_arg]


def find_union(text1: str, text2: str):
    return set2list(set(make_bi_gram(text1) + make_bi_gram(text2)))


def find_intersection(text1: str, text2: str):
    text1_bi_gram = set2list(set(make_bi_gram(text1)))
    text2_bi_gram = set2list(set(make_bi_gram(text2)))
    return set2list(set([bi_gram for bi_gram in text1_bi_gram if bi_gram in text2_bi_gram]
                        + [bi_gram for bi_gram in text2_bi_gram if bi_gram in text1_bi_gram]))


def find_diff_of_sets(text1: str, text2: str):
    return [bi_gram for bi_gram in find_union(text1, text2) if bi_gram not in find_intersection(text1, text2)]


if __name__ == '__main__':
    text1 = "paraparaparadise"
    text2 = "paragraph"
    print(f'bi-gram of text1 => {make_bi_gram(text1)}')
    print(f'bi-gram of text2 => {make_bi_gram(text2)}')
    print(f'union of text1 and text2 => {find_union(text1, text2)}')
    print(f'intersection of text1 and text2 => {find_intersection(text1, text2)}')
    print(f'difference of text1 and text2 => {find_diff_of_sets(text1, text2)}')
