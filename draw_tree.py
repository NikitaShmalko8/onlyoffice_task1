
def draw_tree_func(height, file_path):
    tree = []
    if height < 1:
        raise ValueError('Высота елки должна быть больше 0!')

    for i in range(1):
        tree.append(' ' * (height + 2) + 'W')
        tree.append(' ' * (height + 2) + '*')

    for i in range(1, height + 1):
        if i %2==0:
            tree.append(' ' * (height - i + 1) + '@'+'*' * (2 * i + 3))

        else:
            tree.append(' ' * (height - i + 1) + '*' * (2 * i + 3) + '@')

    for i in range(2):
        tree.append(' ' * (height) + 'TTTTT')

    tree = '\n'.join(tree) + '\n'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(tree)
        print(f'Елка сохранена в файл {file_path}')
