from app.Goods import Goods, Good
import pytest


@pytest.fixture(scope='module')
def goods():
    print('*****SETUP START*****\n')
    goods = Goods()
    print('*****SETUP FINISH*****\n')
    yield goods
    print('******TEARDOWN START******\n')
    print('******TEARDOWN FINISH******\n')


@pytest.fixture(scope='function')
def empty_goods(goods: Goods):
    yield goods
    goods.clear()


@pytest.fixture(scope='function')
def sample_goods(goods: Goods):
    notebook = Good(id=0, name='notebook', stock=50)
    textbook = Good(id=1, name='textbook', stock=40)
    goods.add(notebook)
    goods.add(textbook)
    yield goods
    goods.clear()


def test_add(empty_goods: Goods):
    pen = Good(id=2, name='pen', stock=10)
    eraser = Good(id=3, name='eraser', stock=20)
    assert empty_goods.len() == 0
    empty_goods.add(pen)
    empty_goods.add(eraser)
    assert empty_goods.len() == 2


def test_get_by_id(sample_goods: Goods):
    id = 0
    notebook = sample_goods.get_by_id(id)
    assert notebook.id == id
    assert notebook.name == 'notebook'
    assert notebook.stock == 50


def test_remove_by_id(sample_goods: Goods):
    assert sample_goods.len() == 2
    sample_goods.remove_by_id(0)
    assert sample_goods.len() == 1
    with pytest.raises(Exception):
        sample_goods.get_by_id(0)
