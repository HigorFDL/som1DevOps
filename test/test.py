
from src.main import *

def test_soma(a, b):
    assert soma(2,3) == 5


def test_funcionamento_soma():
    resultado = funcionamento_soma(2, 3)
    assert resultado["resultados"] == 5