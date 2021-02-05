from pytest import fixture
from geometrical_figures import Triangle, Rectangle, Square, Circle


@fixture(params=[Triangle(1, 1),
                 Rectangle(1, 1),
                 Square(1, 1),
                 Circle(1, 1)], scope="session")
def figure(request):
    return request.param


@fixture(params=[Triangle,
                 Rectangle,
                 Square,
                 Circle], scope="session")
def figure_class(request):
    return request.param
