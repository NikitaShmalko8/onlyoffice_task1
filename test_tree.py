from draw_tree import draw_tree_func
import pytest

def test_draw_tree_height_10():
    height = 10
    expected = """            W
            *
          *****@
         @*******
        *********@
       @***********
      *************@
     @***************
    *****************@
   @*******************
  *********************@
 @***********************
          TTTTT
          TTTTT
"""
    draw_tree_func(height, 'tree.txt')
    with open('tree.txt', 'r', encoding='utf-8') as f:
        result = f.read()
    print('\n' + result)
    assert expected == result


def test_draw_tree_height_1():
    height = 1
    expected = """   W
   *
 *****@
 TTTTT
 TTTTT
"""
    draw_tree_func(height, 'tree.txt')
    with open('tree.txt', 'r', encoding='utf-8') as f:
        result = f.read()
    print('\n' + result)
    assert expected == result


def test_draw_tree_zero_height():

    with pytest.raises(ValueError, match="Высота елки должна быть больше 0!"):
        draw_tree_func(0, 'tree.txt')

def test_draw_tree_invalid_path():
    with pytest.raises(OSError):
        draw_tree_func(1, '/invalid_dir/output.txt')










