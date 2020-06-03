# templates
def get_template_sentence(x: int, y: str, z: float):
    return f"{x}時の{y}は{z}"


if __name__ == '__main__':
    print(get_template_sentence(12, '気温', 22.4))
