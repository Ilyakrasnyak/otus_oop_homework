from pytest import raises, mark


def test_necessary_fields_exist(figure):
    assert figure.area == 1
    assert figure.perimeter == 1
    assert figure.name in ["triangle", "rectangle", "square", "circle"]
    assert figure.angles in [4, 3, 0]


@mark.parametrize("init_val", [("one", 1), (2.01, 1), ([1, 2, 3], 1)])
def test_invalid_area_init(figure_class, init_val):
    with raises(ValueError):
        figure_class(init_val[0], init_val[1])


@mark.parametrize("init_val", [(1, "one"), (1, 2.01), (1, [1, 2, 3])])
def test_invalid_perimeter_init(figure_class, init_val):
    with raises(ValueError):
        figure_class(init_val[0], init_val[1])


def test_delete_area(figure):
    with raises(AttributeError):
        del figure.area


def test_delete_perimeter(figure):
    with raises(AttributeError):
        del figure.perimeter


def test_change_name(figure):
    with raises(AttributeError):
        figure.name = 'new_name'


def test_delete_name(figure):
    with raises(AttributeError):
        del figure.name


def test_change_angles(figure):
    with raises(AttributeError):
        figure.angles = 10


def test_delete_angles(figure):
    with raises(AttributeError):
        del figure.angles


def test_add_area(figure, figure_class):
    new_figure = figure_class(2, 2)
    assert new_figure.add_area(figure) == 3


@mark.parametrize("val", [1, "one", 1.1, ['1', 2]])
def test_add_area_with_not_figure(figure, val):
    with raises(TypeError):
        figure.add_area(val)
